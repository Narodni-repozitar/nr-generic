import uuid

import pytest
from invenio_pidstore.models import PersistentIdentifier, PIDStatus

from nr_generic.record import PublishedCommonRecord


def create_draft_record(record: dict, pid_type=None, pid_value=None):
    if not pid_type:
        pid_type = "dnr"
    if not pid_value:
        pid_value = record["control_number"]
    id_ = uuid.uuid4()
    pid = PersistentIdentifier.create(
        pid_type,
        pid_value,
        pid_provider=None,
        object_type="rec",
        object_uuid=id_,
        status=PIDStatus.REGISTERED,
    )
    db_record = PublishedCommonRecord.create(record, id_=id_)
    return db_record


@pytest.mark.usefixtures("app", "db", "taxonomy_tree", "base_json", "base_json_dereferenced")
class TestRecord:
    def test_canonical_url(self, app, db, base_json_dereferenced):
        record = create_draft_record(base_json_dereferenced)
        with app.app_context():
            assert record.canonical_url == "http://127.0.0.1:5000/common/411100"
