from time import time

class Employee :
    #Classe salarié de l'entreprise

    def __init__(self, salary = 0, name = "", sexe = "",  skills = ['python']) :
        self.salary = salary
        self.name = name
        self.sexe = sexe
        self.skills = skills

    def classification(self) :
      job = ['SE', 'DS', 'MLE']
      if self.skills == ['python', 'sql', 'gcp'] :
        return(job[1])
      elif self.skills == ['python', 'react', 'angular', 'js'] :
         return(job[0])
      elif self.skills == ['python', 'sql', 'docker', 'terraform'] :
         return(job[2])



class Senior(Employee) :
  def __init__(self, salary=0, name="", sexe="", skills=[], nb_arrival=5):
    super().__init__(salary, name, sexe, skills)
    self.nb_arrival = nb_arrival 


if __name__ == '__main__' :
  antoine = Senior(salary=3000, name="Antoine", sexe="M", skills=['python', 'sql', 'gcp'], nb_arrival=7)
  print(f"{antoine.name} is a {antoine.classification()}")
  greg = Senior(salary=2450, name="Greg", sexe="M", skills=['python', 'sql', 'docker', 'terraform'], nb_arrival=6)
  print(f"{greg.name} is a {greg.classification()}")
  ibra = Senior(salary=6400, name="Ibra", sexe="M", skills=['python', 'react', 'angular', 'js'], nb_arrival=1)
  print(f"{ibra.name} is a {ibra.classification()}")
  manon = Senior(salary=4700, name="Manon", sexe="F", skills=['python', 'sql', 'gcp'], nb_arrival=8)
  print(f"{manon.name} is a {manon.classification()}")
  steve = Senior(salary=6200, name="Steve", sexe="M", skills=['python', 'react', 'angular', 'js'], nb_arrival=9)
  print(f"{steve.name} is a {steve.classification()}")

  l = [antoine, greg, ibra, manon, steve]

  deb = time()
  m = max(l, key=lambda x : x.nb_arrival)
  print(f"{m.name} est le plus ancien")
  # for i in l :
  #   if antoine.nb_arrival > greg.nb_arrival and antoine.nb_arrival > ibra.nb_arrival and antoine.nb_arrival > manon.nb_arrival and antoine.nb_arrival > steve.nb_arrival :
  #     print(f"The older is {antoine.name} with {antoine.nb_arrival} years in this company")
  #     break
  #   elif greg.nb_arrival > antoine.nb_arrival and greg.nb_arrival > ibra.nb_arrival and greg.nb_arrival > manon.nb_arrival and greg.nb_arrival > steve.nb_arrival :
  #     print(f"The older is {greg.name} with {greg.nb_arrival} years in this company")
  #     break
  #   elif ibra.nb_arrival > antoine.nb_arrival and ibra.nb_arrival > greg.nb_arrival and ibra.nb_arrival > manon.nb_arrival and ibra.nb_arrival > steve.nb_arrival :
  #     print(f"The older is {ibra.name} with {ibra.nb_arrival} years in this company")
  #     break
  #   elif manon.nb_arrival > antoine.nb_arrival and manon.nb_arrival > ibra.nb_arrival and manon.nb_arrival > greg.nb_arrival and manon.nb_arrival > steve.nb_arrival :
  #     print(f"The older is{ manon.name} with {manon.nb_arrival} years in this company")
  #     break
  #   elif steve.nb_arrival > antoine.nb_arrival and steve.nb_arrival > ibra.nb_arrival and steve.nb_arrival > greg.nb_arrival and steve.nb_arrival > manon.nb_arrival :
  #      print(f"The older is {steve.name} with {steve.nb_arrival} years in this company")
  #      break
  fin =time()
  print(f"Execution took {(fin-deb) * 1000} ms")