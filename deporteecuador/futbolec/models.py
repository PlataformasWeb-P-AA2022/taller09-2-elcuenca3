from django.db import models

# Create your models here.

class EquipoF(models.Model):
    
     nombre = models.CharField(max_length=60)
     siglas = models.CharField(max_length=15)
     userTwitter = models.CharField(max_length=60)
    # modulos = models.ManyToManyField('Modulo', through='Matricula')
     def __str__(self):
        return "%s-%s-%s" % (self.nombre,self.siglas,self.userTwitter)


class Jugador (models.Model):
 
 nombre = models.CharField(max_length=30)
 posicion = models.CharField(max_length=30)
 camisa = models.IntegerField("Numero de Camisa")
 sueldo = models.IntegerField("Sueldo")
 equipo_futbol = models.ForeignKey(EquipoF, related_name='losjugadores',
 on_delete=models.CASCADE)

# estudiantes = models.ManyToManyField(Estudiante, through='Matricula')

 def __str__(self):
      return "%s - %s - Camisa: %d - Sueldo: %d - %s" % (self.nombre,self.posicion,
  self.camisa,self.sueldo,self.equipo_futbol)


class Campeonato(models.Model):
    nombreC=models.CharField("Nombre campeonato",max_length=60)
    nombreA=models.CharField("Nombre del Auspiciante",max_length=60)
    


    def __str__(self):
        return "%s - %s " % (self.nombreC, 
                self.nombreA)


class CampeonatoE(models.Model):
    anio= models.CharField(max_length=200)
    ef= models.ForeignKey(EquipoF, related_name='futbol', 
            on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='futbol', 
            on_delete=models.CASCADE)
 
    # modulos = models.ManyToManyField('Modulo', through='Matricula')


    def __str__(self):
        return "%s - %s - %s" % (self.anio, 
                self.ef,
                self.campeonato)

