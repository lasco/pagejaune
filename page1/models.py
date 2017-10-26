from __future__ import unicode_literals

from django.db import models

    
class Secteur(models.Model):
    secteur_nom = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Secteur d'activite"
        verbose_name_plural = "Seteurs dactivites"
    def __unicode__(self):
        return "%s" %(self.secteur_nom)

class Region (models.Model):
	nom_region = models.CharField(max_length= 50, unique= True)
	
	class Meta:
		verbose_name = "Region"
		verbose_name_plural = "Regions"
	def __unicode__(self):
		return "%s" %(self.nom_region)

class Representant(models.Model):
    code_proprietaire = models.CharField(max_length=50,unique = True)
    nom_proprietaire = models.CharField(max_length=20)
    prenom_proprietaire =models.CharField(max_length=15)
    numero_proprietaire = models.IntegerField()
    class Meta:
        verbose_name = "Representant"
        verbose_name_plural = "Representants"
        
    def  __unicode__(self):
        return "%s - %s " %(self.nom_proprietaire,self.prenom_proprietaire)
        

class Entreprise(models.Model):
    proprietaire = models.ForeignKey(Representant,on_delete= models.CASCADE)
    corporate = models.BooleanField()
    entreprise_nom = models.CharField(max_length=50,\
                              verbose_name = "Nom")
    region = models.ForeignKey(Region ,on_delete= models.CASCADE)
    quartier = models.CharField(max_length=20)
    entreprise_adresse = models.TextField(max_length = 200,\
                      verbose_name = "Adresse")
    entreprise_telephone = models.IntegerField()
    entreprise_email = models.EmailField()
    entreprise_secteur = models.ForeignKey(Secteur)
    entreprise_site_web = models.CharField(max_length=50, blank = True) 
    entreprise_service = models.TextField(max_length=200)
    cordonnee_longtitude = models.FloatField(blank = True ,null=True)
    cordonnee_laltitude =  models.FloatField(blank = True ,null=True)
    date_publication = models.DateField(auto_now = True)
    pubication = models.BooleanField()
    
    
    class Meta:
        verbose_name = "Entreprise"
        verbose_name_plural = "Entreprises"
    def __unicode__(self):
        return "%s" %self.entreprise_nom

class Heure_travail(models.Model):
    entreprise = models.ForeignKey(Entreprise,on_delete= models.CASCADE)
    DAY_CHOICE = (('lundi','lundi'),('mardi','mardi'),('mercredi','mercredi'),
                  ('jeudi','jeudi'),('vendredi','vendredi'),('samedi','samedi'),
                  ('dimanche','dimanche'))
    jour = models.CharField(max_length=15,choices=DAY_CHOICE)
    heure_ouverture = models.TimeField()
    heure_fermeture = models.TimeField()
    class Meta:
        verbose_name = "Heure de travail"
    def __unicode__(self):
        return "%s" %(self.entreprise)

class Commentaire(models.Model):
    entreprise = models.ForeignKey(Entreprise,on_delete= models.CASCADE)
    SCORE_CHOICES = tuple([(x, x) for x in range(0, 6)])
    score = models.SmallIntegerField(choices=SCORE_CHOICES)
    commentaire_speudo = models.CharField(max_length=50)
    contenu = models.TextField()
    commentaire_email = models.EmailField()
    class Meta:
        verbose_name = "Commentaire"
    def __unicode__(self):
        
        return "%s" %(self.commentaire_speudo)
class Galerie(models.Model):
    
    entreprise = models.ForeignKey(Entreprise,on_delete= models.CASCADE)
    logo = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    entreprise_local  = models.ImageField(upload_to='uploads/%Y/%m/%d/',blank = True)
    entreprise_activity = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank = True)
    autre  = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank = True)
    class Meta:
        verbose_name = 'Galerie'
        verbose_name_plural = 'Galeries'
    def __unicode__(self):
        return "%s" % self.entreprise
    
