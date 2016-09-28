Sequence-safe postgres backend for Django
=========================================

This is a replacement for the default postgres backend for Django, version 1.7
and newer.

The difference is it discovers sequence names differently, by inspecting the
metadata table ``information_schema.columns`` instead of using the function
``pg_get_serial_sequence()``. The former shows which sequence is currently in use
by a column, while the latter shows which table owns a sequence.

In the common case these two lead to the same sequence, but it is perfectly
possible to have one sequence be used by two diffferent tables (and owned by
only one of them). Furthermore, if a table inherits a column with a sequence,
then ``pg_get_serial_sequence()`` won't find anything for the child table.

Install with pip, and use it in your settings-file::

    DATABASES = {
        'default': {
            'ENGINE': 'dpb.postgres_sequencesafe',
            # other settings
        }
    }
