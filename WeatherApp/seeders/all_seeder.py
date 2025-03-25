from WeatherApp.models import Measures, Users  #Da error y no se por que

#Los seeders no tienen una funcion en este proyecto
#Solo los usamos para comprobar la correcta migracion de los modelos
user1 = Users.objects.create(name = "Rafael", surname = "De la Rosa", email="awdad", password = "awdawd" , phone_number = 921931)