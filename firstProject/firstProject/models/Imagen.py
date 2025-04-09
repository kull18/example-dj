class Imagen():
    palabra = models.CharField(max_length=100)
    url = models.URLField(max_length=300)

    def __str__(self):
        return self.palabra
