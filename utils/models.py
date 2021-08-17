from django.db import models
from datetime import datetime

class BaseModel(models.Model):
    """
    BaseModel acts as an abstract class which another model can inherit from.
    """
    is_deleted = models.BooleanField(
        default=False,
        help_text='Indica si el objeto ha sido eliminado o no.'
    )
    deleted_at = models.DateTimeField(
        null=True,
        help_text='Día y hora en que se eliminó el objeto'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Día y hora de creación del objeto'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text='Día y hora de modificación del objeto'
    )

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()

    class Meta:
        abstract = True