from django.db import models
import uuid
from django.utils import timezone
from activitys import Activity


class Info(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100, null=False)
    endereco = models.CharField(max_length=255)
    area_de_atuacao = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='infos')
    telefone = models.CharField(max_length=20)
    pdf = models.FileField(upload_to='pdfs/')
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.nome
