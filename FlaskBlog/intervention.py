#app.py
from flask import Flask, request, render_template, url_for,send_file,g,url_for, redirect,flash, session

#from flask_uploads import UploadSet, configure_uploads, IMAGES
from FlaskBlog import conn
from FlaskBlog import app

import os


#
class intervention():

	def __init__(self, Nom_Machine, Equipe,Etat, description, Etat_Urgent_Normal):
		self.Nom_Machine = Nom_Machine
		self.Etat = Etat
		self.Date = Date
		
	def GetNom_Machine(self):
		return self.Nom_Machine

	def SetNom_Machine(self,Nom_Machine):
		self.Nom_Machine=Nom_Machine


	def GetEtat(self):
		return self.Etat

	def SetEtat(self,Etat):
		self.Etat=Etat
		
	def GetDate(self):
		return self.Date

	def SetDate(self,D):
		self.Date=Date






	wsgi_app=app.wsgi_app

	# méthode 
	@app.route('/page_add_intervention/',methods=['POST','GET'])
	def page_add_intervention():
		#Session
		if g.user:
		
			cur =conn.cursor()
			cur.execute("SELECT * FROM Machine ")
			data_Machine = cur.fetchall()
			Data_Machine=data_Machine
			
			cur =conn.cursor()
			cur.execute("SELECT * FROM intervention ")
			data_Intervention = cur.fetchall()
			Data_Intervention=data_Intervention
			
			cur =conn.cursor()
			cur.execute("SELECT count(*) FROM notification_intervention_responsable WHERE Login_Operateur=%s",(session['user']))
			data_Nb_Notifivation_Intervention = cur.fetchall()
			Data_Nb_Notifivation_Intervention=data_Nb_Notifivation_Intervention

			cur =conn.cursor()
			cur.execute("SELECT * FROM notification_intervention_responsable WHERE Login_Operateur=%s",(session['user']) )
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

			return render_template("gestion_Demande_intervention.html",Login=session['user'],username=session['name'],Machine=Data_Machine,Data_Nb_Notif_Intervention=var,Interventions=Data_Intervention)
		
		return redirect(url_for('Test_Compte'))	

		

	# méthode 
	@app.route('/Ajouter_Demande_intervention/',methods=['POST','GET'])
	def Ajouter_Demande_intervention():

		try:

			global Log_utilisateur	
			global Nom_utilisateur	
			
			if g.user:
				Log_utilisateur=session['user']
				Nom_utilisateur=session['name']

				if request.method == 'POST':
						
					M = request.form['machine']
					S = request.form['secteur']
					E = request.form['etat']
					D = request.form['description']
					EUN = request.form['etat_u']

					try: 

						#cur = conn.cursor()
						#cur.execute("INSERT INTO intervention VALUES (NULL,%s, %s, %s, %s, %s, %s,%s)", (M,S,E,D,EUN,Nom_utilisateur,Log_utilisateur ))
						#conn.commit()

						cur = conn.cursor()
						cur.execute("INSERT INTO notification_intervention_responsable VALUES (NULL,%s, %s, %s, %s, %s, %s,%s)", (M,S,E,D,EUN,Nom_utilisateur,Log_utilisateur ))
						conn.commit()
						
						#Session
						if g.user:
							flash("intervention Enregistré avec succès")
							return redirect(url_for('page_add_intervention'))	
						return redirect(url_for('Test_Compte'))	

					except Exception as e:
						print (e)

								
			#Session
			if g.user:
				flash("Existe Déja !")
				return redirect(url_for('page_add_intervention'))
			return redirect(url_for('Test_Compte'))	


			#return redirect(url_for('Test_Compte'))	

		except Exception as e:
			print('erreur database: {}'.format(e))
		#return render_template("page_identification.html" , error="enregistrement réfusé")
		#return redirect(url_for('Test_Compte'))
		flash("Vérifier votre données")
		return redirect(url_for('page_add_intervention'))

			


	@app.route('/delete_Demande_intervention/<int:M_data>', methods = ['GET'])
	def delete_Demande_intervention(M_data):

		try:

			cur =conn.cursor()

			sql_P = 'SELECT * FROM notification_intervention_responsable'

			data = cur.execute(sql_P)
			data =cur.fetchone()
			print('***---------******------********')
			print(type(M_data))
			print(data)
			while data is not None :
				print(data)
				if M_data == data[0] :
					print('***---------******------********')
					print(data[0])	
					cur = conn.cursor()
					cur.execute("DELETE FROM notification_intervention_responsable WHERE Id_Notification=%s", (M_data,))
					conn.commit()
					
					if g.user:
						flash("intervention Supprimé avec succès")
						return redirect(url_for('page_add_intervention'))
					return redirect(url_for('Test_Compte'))	
					
				else:
					data = cur.fetchone()

		except Exception as e:
			print('erreur database: {}'.format(e))
			#return redirect(url_for('page_Ajouter_Classe'))




	@app.route('/page_liste_Demande_intervention/',methods=['POST','GET'])
	def page_liste_Demande_intervention():
		#Session
		if g.user:
		
	
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

		
			cur =conn.cursor()
			cur.execute("SELECT * FROM technicien order by  Nb_travail ASC ")
			data_t = cur.fetchall()
			Data_t=data_t
					
			
			return render_template("gestion_envoiyer_demande_intervention.html",Login=session['user'],username=session['name'],Interventions=Data_Intervention,date_techicien=Data_t,Data_Nb_Notif_Intervention=var)
		
		return redirect(url_for('Test_Compte'))	

		


	# méthode 
	@app.route('/Ajouter_intervention_technicien/',methods=['POST','GET'])
	def Ajouter_intervention_technicien():

		try:

			global Log_utilisateur	
			global Nom_utilisateur	
			
			if g.user:
				Log_utilisateur=session['user']
				Nom_utilisateur=session['name']

				if request.method == 'POST':
					I=request.form['id_notif']
					M = request.form['machine']
					S = request.form['secteur']
					D = request.form['description']
					EUN = request.form['etat_u']
					T = request.form['technicien']
					Date_int= request.form['date_interv_souhaitee']
					print(I)
					print(M)
					print(S)
					print(D)
					print(EUN)
					print(T)
					print(Date_int)


					try: 

						cur = conn.cursor()
						cur.execute("DELETE FROM notification_intervention_responsable WHERE Id_Notification=%s", (I,))
						conn.commit()

						cur = conn.cursor()
						cur.execute("INSERT INTO notification_intervention_responsable_to_tevhnicien VALUES (NULL,%s, %s, %s, %s, %s, %s, %s)", (M,S,D,EUN,Date_int,T,Log_utilisateur ))
						conn.commit()
						
						#Session
						if g.user:
							flash("intervention Enregistré avec succès")
							return redirect(url_for('page_liste_Demande_intervention'))	
						return redirect(url_for('Test_Compte'))	

					except Exception as e:
						print (e)

								
			#Session
			if g.user:
				flash("Existe Déja !")
				return redirect(url_for('page_liste_Demande_intervention'))
			return redirect(url_for('Test_Compte'))	


			#return redirect(url_for('Test_Compte'))	

		except Exception as e:
			print('erreur database: {}'.format(e))
		#return render_template("page_identification.html" , error="enregistrement réfusé")
		#return redirect(url_for('Test_Compte'))
		flash("Vérifier votre données")
		return redirect(url_for('page_liste_Demande_intervention'))




	@app.route('/page_liste_recoit_intervention/',methods=['POST','GET'])
	def page_liste_recoit_intervention():
		#Session
		if g.user:
			
			cur =conn.cursor()
			cur.execute("SELECT count(*) FROM notification_intervention_responsable_to_tevhnicien  WHERE Login_Technicien=%s",(session['user']))
			data_Nb_Notifivation_Intervention = cur.fetchall()
			Data_Nb_Notifivation_Intervention=data_Nb_Notifivation_Intervention

			
			cur =conn.cursor()
			cur.execute("SELECT count(*) FROM planification_maintenance WHERE Login_Technicien=%s",(session['user']))
			data_Nb_Planification = cur.fetchall()
			Data_Nb_Planificationn=data_Nb_Planification

			var2=0
			for x in Data_Nb_Planificationn :
				print(x)
				for y in x:
					var2=y
			print("*********")
			print(var2)


			cur =conn.cursor()
			cur.execute("SELECT * FROM notification_intervention_responsable_to_tevhnicien  WHERE Login_Technicien=%s",(session['user']))
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


			return render_template("gestion_recoit_demande_intervention.html",Login=session['user'],username=session['name'],Data_Nb_Notif_Intervention=var,Interventions=Data_Intervention,Data_Nb_Planificationn=var2)
		
		return redirect(url_for('Test_Compte'))	

		