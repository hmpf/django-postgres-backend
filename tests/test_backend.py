import copy

from django.conf import settings
from django.db import connection, connections, DEFAULT_DB_ALIAS
from django.db.utils import ConnectionHandler
from django.test import TestCase

from postgres_legacy.base import get_sequence_name

from tests.models import *


class SequenceChangeTestCase(TestCase):

    def tearDown(self):
        try:
            cursor = connection.cursor()
            cursor.execute("""ALTER TABLE tests_contractedservice
                    ALTER COLUMN id
                    SET DEFAULT nextval('tests_contractedservice_id_seq');""")
        except:
            raise
    setUp = tearDown

    def test_get_sequence_name(self):
        cursor = connection.cursor()
        sequence_name = get_sequence_name(cursor, 'tests_service', 'id')
        self.assertEqual(sequence_name, 'tests_service_id_seq')

    def test_change_sequence_name(self):
        # different sequences should lead to identical sets of ids
        for c in ('a', 'b', 'c'):
            Service.objects.create(service_name=c)
            ContractedService.objects.create(service_name='Contracted '+c)
        service_ids = Service.objects.values_list('id', flat=True)
        contracted_service_ids = ContractedService.objects.values_list('id', flat=True)
        self.assertEqual(set(service_ids), set((1, 2, 3,)))
        self.assertEqual(set(service_ids), set(contracted_service_ids))

        # sharing a sequence should make the ids different
        cursor = connection.cursor()
        cursor.execute("""ALTER TABLE tests_contractedservice
                ALTER COLUMN id
                SET DEFAULT nextval('tests_service_id_seq');""")
        for c in ('d', 'e', 'f'):
            Service.objects.create(service_name=c)
            ContractedService.objects.create(service_name='Contracted '+c)
        service_ids = Service.objects.values_list('id', flat=True)
        contracted_service_ids = ContractedService.objects.values_list('id', flat=True)
        self.assertNotEqual(set(service_ids), set(contracted_service_ids))

        # the last_insert_id should be the same, pointing to the same sequence
        last_insert_id1 = connection.ops.last_insert_id(cursor, 'tests_service', 'id')
        last_insert_id2 = connection.ops.last_insert_id(cursor, 'tests_contractedservice', 'id')
        self.assertEqual(last_insert_id1, last_insert_id2)
