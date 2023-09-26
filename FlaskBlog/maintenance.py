#app.py
from flask import Flask, request, render_template, url_for,send_file,g,url_for, redirect,flash, session

#from flask_uploads import UploadSet, configure_uploads, IMAGES
from FlaskBlog import conn
from FlaskBlog import app

import os


#
class maintenance():

	def __init__(self, Nom_Machine, Etat, Date):
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
	@app.route('/page_add_planification_maintenance/',methods=['POST','GET'])
	def page_add_planification_maintenance():
		#Session
		if g.user:

			Log_utilisateur=session['user']
		
			cur =conn.cursor()
			cur.execute("SELECT * FROM Machine ")
			data_Machine = cur.fetchall()
			Data_Machine=data_Machine
			
			cur =conn.cursor()
			cur.execute("SELECT * FROM planification_maintenance  WHERE Login_Technicien=%s",(Log_utilisateur))
			data_Planification = cur.fetchall()
			Data_Planification=data_Planification
			
			
			cur =conn.cursor()
			cur.execute("SELECT count(*) FROM planification_maintenance WHERE Login_Technicien=%s",(Log_utilisateur))
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
			cur.execute("SELECT count(*) FROM notification_intervention_responsable_to_tevhnicien WHERE Login_Technicien=%s",(Log_utilisateur))
			data_Nb_Notifivation_Intervention = cur.fetchall()
			Data_Nb_Notifivation_Intervention=data_Nb_Notifivation_Intervention

			cur =conn.cursor()
			cur.execute("SELECT * FROM notification_intervention_responsable_to_tevhnicien WHERE Login_Technicien=%s",(Log_utilisateur))
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


			return render_template("gestion_Planification_Maintenance.html",Login=session['user'],username=session['name'],Data_Nb_Notif_Intervention=var,Interventions=Data_Intervention,Machine=Data_Machine,Planification_Maintenance=Data_Planification,Nb_Data_Nb_Planificationn=var2)
		
		return redirect(url_for('Test_Compte'))	

		

	# méthode 
	@app.route('/Ajouter_Planification_Maintenance/',methods=['POST','GET'])
	def Ajouter_Planification_Maintenance():

		try:

			global Log_utilisateur	
			global Nom_utilisateur	
			
			if g.user:
				Log_utilisateur=session['user']
				Nom_utilisateur=session['name']

				if request.method == 'POST':
						
					M = request.form['machine']
					E = request.form['etat']
					DP = request.form['datePlaification']

					try: 

						cur = conn.cursor()
						cur.execute("INSERT INTO planification_maintenance VALUES (NULL,%s, %s, %s, %s, %s)", (M,E,DP,Nom_utilisateur,Log_utilisateur ))
						conn.commit()
						
						#Session
						if g.user:
							flash("Planification de maintenance de " + M + " Enregistré avec succès")
							return redirect(url_for('page_add_planification_maintenance'))	
						return redirect(url_for('Test_Compte'))	

					except Exception as e:
						print (e)

								
			#Session
			if g.user:
				flash("Existe Déja !")
				return redirect(url_for('page_add_planification_maintenance'))
			return redirect(url_for('Test_Compte'))	


			#return redirect(url_for('Test_Compte'))	

		except Exception as e:
			print('erreur database: {}'.format(e))
		#return render_template("page_identification.html" , error="enregistrement réfusé")
		#return redirect(url_for('Test_Compte'))
		flash("Vérifier votre données")
		return redirect(url_for('page_add_planification_maintenance'))

			


	@app.route('/delete_Planification_Maintenance/<int:M_data>', methods = ['GET'])
	def delete_Planification_Maintenance(M_data):

		try:

			cur =conn.cursor()

			sql_P = 'SELECT * FROM planification_maintenance'

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
					cur.execute("DELETE FROM planification_maintenance WHERE id=%s", (M_data,))
					conn.commit()
					
					if g.user:
						flash("Planification de maintenance Supprimé avec succès")
						return redirect(url_for('page_add_planification_maintenance'))
					return redirect(url_for('Test_Compte'))	
					
				else:
					data = cur.fetchone()

		except Exception as e:
			print('erreur database: {}'.format(e))
			#return redirect(url_for('page_Ajouter_Classe'))




