from flask import render_template, request, redirect, url_for ,flash, session, g
from FlaskBlog import conn


from FlaskBlog import app

Log=""



#Class Compte
class Compte():

	def __init__(self,Login,Mdp):
		self.Login = Login
		self.Mdp = Mdp

	def GetLogin(self):
		return self.Login

	def SetLogin(self,Login):
		self.Login=Login


	def GetMdp(self):
		return self.Mdp

	def SetMdp(self,Mdp):
		self.Mdp=Mdp
		



	# 
	@app.route('/',methods=['POST','GET'])
	def Test_Compte():

		try:
			if request.method == 'POST':

				session.pop('user', None)

				global Log
				
				Log = request.form['Login']

				cur =conn.cursor()

				donnees_super_R = 'SELECT * FROM super_responsable'
				donnees_T =  'SELECT * FROM Technicien'
				donnees_O =  'SELECT * FROM Operateur'
				donnees_R =  'SELECT * FROM Responsable'

				data = cur.execute(donnees_super_R)
				data =cur.fetchone()

				while data is not None :

					if int(Log) == data[0]  and request.form['Mdp'] == data[1] :

							session['user'] = str(data[0])
							session['name'] = str(data[2])+" "+str(data[3])

					
							return render_template("page_Accueil_SuperResponsable.html", Login=session['user'],username=session['name'])
					else:
						data = cur.fetchone()
					
				

				data =cur.execute(donnees_T)
				data = cur.fetchone()

				while data is not None :

					if int(Log)== data[0]  and request.form['Mdp'] == data[1] :

							session['user'] = str(data[0])
							session['name'] = str(data[2])+" "+str(data[3])



							cur =conn.cursor()
							cur.execute("SELECT count(*) FROM notification_intervention_responsable_to_tevhnicien  WHERE Login_Technicien=%s",(session['user']))
							data_Nb_Notifivation_Intervention = cur.fetchall()
							Data_Nb_Notifivation_Intervention=data_Nb_Notifivation_Intervention

							cur =conn.cursor()
							cur.execute("SELECT * FROM notification_intervention_responsable_to_tevhnicien WHERE Login_Technicien=%s",(session['user']))
							data_Intervention = cur.fetchall()
							Data_Intervention=data_Intervention
							print(Data_Nb_Notifivation_Intervention)
							var=0
							for x in Data_Nb_Notifivation_Intervention :
								print(x)
								for y in x:
									var=y
							print("*********")
							print(var)


							return render_template("page_Accueil_technicien.html", Login=session['user'],username=session['name'],Data_Nb_Notif_Intervention=var,Interventions=Data_Intervention)

					else:
						data = cur.fetchone()
					


				data =cur.execute(donnees_O)
				data = cur.fetchone()

				while data is not None :

					if int(Log)== data[0]  and request.form['Mdp'] == data[1] :

							session['user'] = str(data[0])
							session['name'] = str(data[2])+" "+str(data[3])
							return render_template("page_Accueil_operateur.html", Login=session['user'],username=session['name'])
					else:
						data = cur.fetchone()
					


				data =cur.execute(donnees_R)
				data = cur.fetchone()

				while data is not None :

					if int(Log)== data[0]  and request.form['Mdp'] == data[1] :

							session['user'] = str(data[0])
							session['name'] = str(data[2])+" "+str(data[3])


							cur =conn.cursor()
							cur.execute("SELECT count(*) FROM notification_intervention_responsable ")
							data_Nb_Notifivation_Intervention = cur.fetchall()
							Data_Nb_Notifivation_Intervention=data_Nb_Notifivation_Intervention

							cur =conn.cursor()
							cur.execute("SELECT * FROM notification_intervention_responsable ")
							data_Intervention = cur.fetchall()
							Data_Intervention=data_Intervention
							print(Data_Nb_Notifivation_Intervention)
							var=0
							for x in Data_Nb_Notifivation_Intervention :
								print(x)
								for y in x:
									var=y
							print("*********")
							print(var)

							return render_template("page_Accueil_responsable.html", Login=session['user'],username=session['name'],Data_Nb_Notif_Intervention=var,Data_Intervention=Data_Intervention)
					else:
						data = cur.fetchone()
					
				else:
					error = "Invalid login ou password"
					return render_template("page_identification.html" , error=error)

			return render_template("page_identification.html")


		except Exception as e:
			print('erreur database: {}'.format(e))

		#session.pop('user', None)
		return render_template("page_identification.html")


