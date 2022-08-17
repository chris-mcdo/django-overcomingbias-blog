import datetime

import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from obapi.models import (
    SEQUENCE_SLUG_MAX_LENGTH,
    EssayContentItem,
    Sequence,
    SpotifyContentItem,
    YoutubeContentItem,
)
from obapi.utils import to_slug


@pytest.mark.django_db
class TestCreateSequence:
    def test_can_create_empty_sequence(self):
        # Arrange
        seq_title = "Empty Sequence"
        # Act
        Sequence.objects.create(title=seq_title, abstract="Description")
        # Assert
        seq = Sequence.objects.get(title=seq_title)
        assert seq.slug == to_slug(seq_title, max_length=SEQUENCE_SLUG_MAX_LENGTH)
        assert not seq.items.all().exists()

        # Act - modify title
        new_title = "New Title"
        seq.title = new_title
        seq.save()
        assert seq.slug == to_slug(new_title, max_length=SEQUENCE_SLUG_MAX_LENGTH)

    def test_can_create_normal_sequence(self):
        # Arrange
        now = datetime.datetime.now()
        video = YoutubeContentItem.objects.create(
            title="YouTube Item", item_id="4yZKGbq1YmA", publish_date=now
        )
        audio = SpotifyContentItem.objects.create(
            title="Spotify Item", item_id="6z8lvJia3OzcIVCStbmEtU", publish_date=now
        )
        text = EssayContentItem.objects.create(
            title="Essay Item", item_id="example", publish_date=now
        )
        seq_title = "Example Sequence"

        # Act - create basic sequence
        seq = Sequence.objects.create(title=seq_title)
        seq.items.add(video, audio, text)

        # Assert
        seq = Sequence.objects.get(title=seq_title)
        assert seq.title == seq_title
        assert seq.items.count() == 3

        # Act - delete one item
        video.delete()
        del video

        # Assert
        seq = Sequence.objects.get(title=seq_title)
        assert seq.title == seq_title
        assert seq.items.count() == 2


@pytest.mark.django_db
class TestSlugUniquenessIsEnforced:
    def test_duplicate_slug_does_not_save(self):
        # Act & Assert - sequence with owner
        Sequence.objects.create(title="Example Sequence")
        with pytest.raises(IntegrityError):
            Sequence.objects.create(title="example-Sequence")

    def test_duplicate_slug_does_not_validate(self):
        # Act & Assert
        Sequence.objects.create(title="Example Sequence")
        seq2 = Sequence(title="example-Sequence")
        with pytest.raises(ValidationError):
            seq2.full_clean()
