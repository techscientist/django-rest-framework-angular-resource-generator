from django.test import TestCase, RequestFactory
from django.conf import settings
import json, os

from drf_ng_generator import schemas
from drf_ng_generator.converter import SchemaConverter



with open(os.path.join(settings.BASE_DIR, 'tests', 'rest_schema.json')) as f:
    REST_SCHEMA = json.load(f)


class TestGenerator(TestCase):

    def test_generator(self):
        generator = schemas.SchemaGenerator()
        schema = generator.get_schema()
        converter = SchemaConverter()
        rest_schema = converter.convert(schema)

        self.assertEqual(
            rest_schema,
            REST_SCHEMA
        )
