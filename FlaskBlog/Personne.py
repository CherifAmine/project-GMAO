from flask import render_template, request, redirect, url_for ,flash, session, g
from FlaskBlog import conn

from FlaskBlog import app
from FlaskBlog import Compte


Data_select=""
log = ""
mdp = ""
nom = ""
prenom ="" 
email = ""
n_tel = ""
code = ""
test="false"


#classe Personne
class Personne():

	def __init__(self, Login, Mdp, Nom,Prenom, Email, N_Tel, Code):
		self.Login = Login
		self.Mdp = Mdp
		self.Nom = Nom
		self.Prenom = Prenom
		self.Email = Email
		self.N_Tel = N_Tel
		self.Code = Code

	def GetLogin(self):
		return self.Login

	def SetLogin(self,Login):
		self.Login=Login


	def GetMdp(self):
		return self.Mdp

	def SetMdp(self,Mdp):
		self.Mdp=Mdp
		
	def GetNom(self):
		return self.Nom

	def SetNom(self,Nom):
		self.Nom=Nom

	def GetPrenom(self):
		return self.Prenom

	def SetPrenom(self,Prenom):
		self.Prenom=Prenom

	def GetEmail(self):
		return self.Email

	def SetEmail(self,Email):
		self.Email=Email

	def GetN_Tel(self):
		return self.N_Tel

	def SetN_Tel(self,N_Tel):
		self.N_Tel=N_Tel

	def GetCode(self):
		return self.Code

	def SetCode(self,Code):
		self.Code=Code


	# méthode 
	@app.route('/AjouterCompte',methods=['POST','GET'])
	def AjouterCompte():

		try:

			global Data_select
			global log
			global mdp
			global nom
			global prenom
			global email
			global n_tel
			global code

			
			if request.method == 'POST':
					
					
					#
					data_select=request.form['data_select']
					
					L = request.form['Login']
					M= request.form['Mdp']
					N = request.form['Nom']
					P = request.form['Prenom']
					E = request.form['Email']
					N_T = request.form['N_Tel']
					C = request.form['Code']
					
				
					Data_select=data_select
					log = L
					mdp = M
					nom = N
					prenom = P 
					email = E
					n_tel=N_T
					code = C

					print(Data_select)
					print(log)
					print(mdp)
					print(nom)
					print(prenom)
					print(email)
					print(n_tel)
					print(code)

					cur =conn.cursor()

					donnees_T =  'SELECT * FROM Technicien'
					donneer_O = 'SELECT * FROM Operateur'
					donneer_R = 'SELECT * FROM Responsable'

					data = cur.execute(donnees_T)
					data = cur.fetchone()
					
					if Data_select == "Technicien" :
						print("Technicien")
						while data is not None :

							if int(log)== data[0] :
								try:
							
									cur = conn.cursor()
									cur.execute("""
									  		UPDATE Technicien
									  		SET  Mdp=%s, Nom=%s, Prenom =%s, Email=%s, N_tel=%s, Nb_travail=%s
									  		WHERE Login_Technicien =%s"""
										, (mdp, nom, prenom, email, n_tel, code, log))

									conn.commit()

									test="true"
									
									#return render_template("page_identification.html" , error="enregistrement avec succées")
									return redirect(url_for('Test_Compte'))
								except Exception as e:
									print (e)	

							else:
								data = cur.fetchone()

					elif Data_select == "Operateur":

						data = cur.execute(donneer_O)
						data = cur.fetchone()
						
						print("Operateur")
						while data is not None :

							if int(log)== data[0] :
								try:
							
									cur = conn.cursor()
									cur.execute("""
									  		UPDATE Operateur
									  		SET  Mdp=%s, Nom=%s, Prenom =%s, Email=%s, N_tel=%s, Nb_travail=%s
									  		WHERE Login_Operateur =%s"""
										, (mdp, nom, prenom, email, n_tel, code, log))

									conn.commit()
									test="true"
									#return render_template("page_identification.html" , error="enregistrement avec succées")
									return redirect(url_for('Test_Compte'))
								except Exception as e:
									print (e)	

							else:
								data = cur.fetchone()
					else :

						data = cur.execute(donneer_R)
						data = cur.fetchone()
						
						print("Responsable")
						while data is not None :

							if int(log)== data[0] :
								try:
							
									cur = conn.cursor()
									cur.execute("""
									  		UPDATE Responsable
									  		SET  Mdp=%s, Nom=%s, Prenom =%s, Email=%s, N_tel=%s, Nb_travail=%s
									  		WHERE Login_Responsable =%s"""
										, (mdp, nom, prenom, email, n_tel, code, log))

									conn.commit()
									test="true"
									#return render_template("page_identification.html" , error="enregistrement avec succées")
									return redirect(url_for('Test_Compte'))
								except Exception as e:
									print (e)	

							else:
								data = cur.fetchone()
		#	
		except Exception as e:
			print('erreur database: {}'.format(e))
		#return render_template("page_identification.html" , error="enregistrement réfusé")
		return redirect(url_for('Test_Compte'))



	
	# méthode 
	@app.route('/page_add_user/',methods=['POST','GET'])
	def page_add_user():
		#Session
		if g.user:
			#cur =conn.cursor()
			#cur.execute("SELECT * FROM classe ")
			#data_Classe = cur.fetchall()
			#Data_CLASSE=data_Classe
			cur =conn.cursor()
			cur.execute("SELECT count(*) FROM technicien ")
			data_Nb_Tech = cur.fetchall()
			Data_Nb_Tech=data_Nb_Tech

			for x in Data_Nb_Tech :
				print(x)
				for y in x:
					var1=y
			print("*********")
			print(var1)




			cur =conn.cursor()
			cur.execute("SELECT count(*) FROM Operateur ")
			data_Nb_O = cur.fetchall()
			Data_Nb_O=data_Nb_O

			for x in Data_Nb_O :
				print(x)
				for y in x:
					var2=y
			print("*********")
			print(var2)





			cur =conn.cursor()
			cur.execute("SELECT count(*) FROM Responsable ")
			data_Nb_R = cur.fetchall()
			Data_Nb_R=data_Nb_R

			for x in Data_Nb_R :
				print(x)
				for y in x:
					var3=y
			print("*********")
			print(var3)





			cur =conn.cursor()
			cur.execute("SELECT count(*) FROM super_responsable ")
			data_Nb_SR = cur.fetchall()
			Data_Nb_SR=data_Nb_SR
		
			for x in Data_Nb_SR :
				print(x)
				for y in x:
					var4=y
			print("*********")
			print(var4)



			return render_template("ajouter_personne.html",Login=session['user'],username=session['name'],var1=var1,var2=var2,var3=var3,var4=var4)
		
		return redirect(url_for('Test_Compte'))	


	
	# méthode 
	@app.route('/Gestion_personne/',methods=['POST','GET'])
	def Gestion_personne():
		#Session
		if g.user:
			cur =conn.cursor()
			cur.execute("SELECT count(*) FROM Technicien ")
			data_Nb_Tech = cur.fetchall()
			Data_Nb_Tech=data_Nb_Tech

			for x in Data_Nb_Tech :
				print(x)
				for y in x:
					var1=y
			print("*********")
			print(var1)




			cur =conn.cursor()
			cur.execute("SELECT count(*) FROM Operateur ")
			data_Nb_O = cur.fetchall()
			Data_Nb_O=data_Nb_O

			for x in Data_Nb_O :
				print(x)
				for y in x:
					var2=y
			print("*********")
			print(var2)





			cur =conn.cursor()
			cur.execute("SELECT count(*) FROM Responsable ")
			data_Nb_R = cur.fetchall()
			Data_Nb_R=data_Nb_R

			for x in Data_Nb_R :
				print(x)
				for y in x:
					var3=y
			print("*********")
			print(var3)





			cur =conn.cursor()
			cur.execute("SELECT count(*) FROM super_responsable ")
			data_Nb_SR = cur.fetchall()
			Data_Nb_SR=data_Nb_SR

			for x in Data_Nb_SR :
				print(x)
				for y in x:
					var4=y
			print("*********")
			print(var4)



			return render_template("gestion_personne.html",Login=session['user'],username=session['name'],var1=var1,var2=var2,var3=var3,var4=var4)
		return redirect(url_for('Test_Compte'))	




	# méthode 
	@app.route('/Ajouter_CIN_Personne/',methods=['POST','GET'])
	def Ajouter_CIN_Personne():

		try:

			global Log_utilisateur	
			global Nom_utilisateur	
			
			if g.user:
				Log_utilisateur=session['user']
				Nom_utilisateur=session['name']

				if request.method == 'POST':

						Data_select=request.form['data_select']
						
						L = request.form['Login']

						if Data_select == "Technicien" :

							print(Log_utilisateur)
							print(Nom_utilisateur)
							print(Data_select)
							print(L)
							try: 

									
								cur = conn.cursor()
								cur.execute("INSERT INTO technicien VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (L,"","","","",0,0,Log_utilisateur ))
								conn.commit()

								cur =conn.cursor()
								cur.execute("SELECT count(*) FROM Technicien ")
								data_Nb_Tech = cur.fetchall()
								Data_Nb_Tech=data_Nb_Tech
								
								for x in Data_Nb_Tech :
									print(x)
									for y in x:
										var1=y
								print("*********")
								print(var1)




								cur =conn.cursor()
								cur.execute("SELECT count(*) FROM Operateur ")
								data_Nb_O = cur.fetchall()
								Data_Nb_O=data_Nb_O
								
								for x in Data_Nb_O :
									print(x)
									for y in x:
										var2=y
								print("*********")
								print(var2)





								cur =conn.cursor()
								cur.execute("SELECT count(*) FROM Responsable ")
								data_Nb_R = cur.fetchall()
								Data_Nb_R=data_Nb_R
								
								for x in Data_Nb_R :
									print(x)
									for y in x:
										var3=y
								print("*********")
								print(var3)





								cur =conn.cursor()
								cur.execute("SELECT count(*) FROM super_responsable ")
								data_Nb_SR = cur.fetchall()
								Data_Nb_SR=data_Nb_SR
								
								for x in Data_Nb_SR :
									print(x)
									for y in x:
										var4=y
								print("*********")
								print(var4)



								
								#Session
								if g.user:
									flash("Technicien Enregistré avec succès")
									return render_template("Ajouter_personne.html", Login=Log_utilisateur,username=Nom_utilisateur,var1=var1,var2=var2,var3=var3,var4=var4)
								return redirect(url_for('Test_Compte'))	

							except Exception as e:
								print (e)


						else :
							if Data_select == "Operateur":
								
								try: 
										
									cur = conn.cursor()
									cur.execute("INSERT INTO Operateur VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (L,"","","","",0,0,Log_utilisateur ))
									conn.commit()

									cur =conn.cursor()
									cur.execute("SELECT count(*) FROM Technicien ")
									data_Nb_Tech = cur.fetchall()
									Data_Nb_Tech=data_Nb_Tech
									
									for x in Data_Nb_Tech :
										print(x)
										for y in x:
											var1=y
									print("*********")
									print(var1)




									cur =conn.cursor()
									cur.execute("SELECT count(*) FROM Operateur ")
									data_Nb_O = cur.fetchall()
									Data_Nb_O=data_Nb_O
									
									for x in Data_Nb_O :
										print(x)
										for y in x:
											var2=y
									print("*********")
									print(var2)





									cur =conn.cursor()
									cur.execute("SELECT count(*) FROM Responsable ")
									data_Nb_R = cur.fetchall()
									Data_Nb_R=data_Nb_R
									
									for x in Data_Nb_R :
										print(x)
										for y in x:
											var3=y
									print("*********")
									print(var3)





									cur =conn.cursor()
									cur.execute("SELECT count(*) FROM super_responsable ")
									data_Nb_SR = cur.fetchall()
									Data_Nb_SR=data_Nb_SR
									
									for x in Data_Nb_SR :
										print(x)
										for y in x:
											var4=y
									print("*********")
									print(var4)




									#Session
									if g.user:
										flash("Operateur Enregistré avec succès")
										return render_template("Ajouter_personne.html", Login=Log_utilisateur,username=Nom_utilisateur,var1=var1,var2=var2,var3=var3,var4=var4)
									return redirect(url_for('Test_Compte'))	

								except Exception as e:
									print (e)
							
							else:
								if Data_select == "Responsable":
									try: 
											
										cur = conn.cursor()
										cur.execute("INSERT INTO Responsable VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (L,"","","","",0,0,Log_utilisateur ))
										conn.commit()

										cur =conn.cursor()
										cur.execute("SELECT count(*) FROM Technicien ")
										data_Nb_Tech = cur.fetchall()
										Data_Nb_Tech=data_Nb_Tech
										
										for x in Data_Nb_Tech :
											print(x)
											for y in x:
												var1=y
										print("*********")
										print(var1)




										cur =conn.cursor()
										cur.execute("SELECT count(*) FROM Operateur ")
										data_Nb_O = cur.fetchall()
										Data_Nb_O=data_Nb_O
										
										for x in Data_Nb_O :
											print(x)
											for y in x:
												var2=y
										print("*********")
										print(var2)





										cur =conn.cursor()
										cur.execute("SELECT count(*) FROM Responsable ")
										data_Nb_R = cur.fetchall()
										Data_Nb_R=data_Nb_R
										
										for x in Data_Nb_R :
											print(x)
											for y in x:
												var3=y
										print("*********")
										print(var3)





										cur =conn.cursor()
										cur.execute("SELECT count(*) FROM super_responsable ")
										data_Nb_SR = cur.fetchall()
										Data_Nb_SR=data_Nb_SR
										
										for x in Data_Nb_SR :
											print(x)
											for y in x:
												var4=y
										print("*********")
										print(var4)



										#Session
										if g.user:
											flash("Responsable Enregistré avec succès")
											return render_template("Ajouter_personne.html", Login=Log_utilisateur,username=Nom_utilisateur,var1=var1,var2=var2,var3=var3,var4=var4)
										return redirect(url_for('Test_Compte'))	

									except Exception as e:
										print (e)
								
			#Session
			if g.user:

				cur =conn.cursor()
				cur.execute("SELECT count(*) FROM Technicien ")
				data_Nb_Tech = cur.fetchall()
				Data_Nb_Tech=data_Nb_Tech
				
				for x in Data_Nb_Tech :
					print(x)
					for y in x:
						var1=y
				print("*********")
				print(var1)




				cur =conn.cursor()
				cur.execute("SELECT count(*) FROM Operateur ")
				data_Nb_O = cur.fetchall()
				Data_Nb_O=data_Nb_O
				
				for x in Data_Nb_O :
					print(x)
					for y in x:
						var2=y
				print("*********")
				print(var2)





				cur =conn.cursor()
				cur.execute("SELECT count(*) FROM Responsable ")
				data_Nb_R = cur.fetchall()
				Data_Nb_R=data_Nb_R
				
				for x in Data_Nb_R :
					print(x)
					for y in x:
						var3=y
				print("*********")
				print(var3)





				cur =conn.cursor()
				cur.execute("SELECT count(*) FROM super_responsable ")
				data_Nb_SR = cur.fetchall()
				Data_Nb_SR=data_Nb_SR
				
				for x in Data_Nb_SR :
					print(x)
					for y in x:
						var4=y
				print("*********")
				print(var4)



				flash("Existe Déja !")
				return render_template("Ajouter_personne.html", Login=Log_utilisateur,username=Nom_utilisateur,var1=var1,var2=var2,var3=var3,var4=var4)
			return redirect(url_for('Test_Compte'))	


			#return redirect(url_for('Test_Compte'))	

		except Exception as e:
			print('erreur database: {}'.format(e))
		#return render_template("page_identification.html" , error="enregistrement réfusé")
		#return redirect(url_for('Test_Compte'))
		flash("Vérifier votre données")
		return render_template("page_Accueil_SuperResponsable.html", Login=Log_utilisateur,username=Nom_utilisateur)



	#
	@app.route('/GetPersonne/<string:Login_data>',methods=['POST','GET'])
	def GetPersonne(Login_data):
		
		try:

			global Log
			global Select_Personne

			try:
				Log = Login_data
				Personne_Select=request.form['Select_Personne']
				Select_Personne= Personne_Select

				if g.user:
					return redirect(url_for('Aff_Personne'))
				return redirect(url_for('Test_Compte'))	
	
			except Exception as e:
				print('erreur database: {}'.format(e))

			#return redirect(url_for('Persones'))

		except Exception as e:
			print('erreur database: {}'.format(e))

		error = "Erreur-Get-Personne"
		return render_template("page_identification.html" , error=error)



	#
	@app.route('/Aff_Personne',methods=['POST','GET'])
	def Aff_Personne():		

		try:
			
			#Session	
			if g.user:


				cur =conn.cursor()
				cur.execute("SELECT count(*) FROM Technicien ")
				data_Nb_Tech = cur.fetchall()
				Data_Nb_Tech=data_Nb_Tech
				
				for x in Data_Nb_Tech :
					print(x)
					for y in x:
						var1=y
				print("*********")
				print(var1)




				cur =conn.cursor()
				cur.execute("SELECT count(*) FROM Operateur ")
				data_Nb_O = cur.fetchall()
				Data_Nb_O=data_Nb_O
				
				for x in Data_Nb_O :
					print(x)
					for y in x:
						var2=y
				print("*********")
				print(var2)





				cur =conn.cursor()
				cur.execute("SELECT count(*) FROM Responsable ")
				data_Nb_R = cur.fetchall()
				Data_Nb_R=data_Nb_R
				
				for x in Data_Nb_R :
					print(x)
					for y in x:
						var3=y
				print("*********")
				print(var3)





				cur =conn.cursor()
				cur.execute("SELECT count(*) FROM super_responsable ")
				data_Nb_SR = cur.fetchall()
				Data_Nb_SR=data_Nb_SR
				
				for x in Data_Nb_SR :
					print(x)
					for y in x:
						var4=y
				print("*********")
				print(var4)



				if Select_Personne=="Technicien":



					cur =conn.cursor()
					cur.execute("SELECT * FROM Technicien ")
					data_Ensg = cur.fetchall()
					Data_Ensg=data_Ensg
					print(Data_Ensg)
					return render_template('Gestion_Personne.html',Login=session['user'],username=session['name'],Personnes=Data_Ensg,var1=var1,var2=var2,var3=var3,var4=var4)

				elif Select_Personne=="Operateur":

					cur =conn.cursor()
					cur.execute("SELECT * FROM Operateur")
					data_etud = cur.fetchall()
					Data_etud = data_etud
					return render_template('Gestion_Personne.html',Login=session['user'],username=session['name'],Personnes=Data_etud,var1=var1,var2=var2,var3=var3,var4=var4)
	
				elif Select_Personne=="Responsable":

					cur =conn.cursor()
					cur.execute("SELECT * FROM Responsable")
					data_etud = cur.fetchall()
					Data_etud = data_etud
					return render_template('Gestion_Personne.html',Login=session['user'],username=session['name'],Personnes=Data_etud,var1=var1,var2=var2,var3=var3,var4=var4)

				else:

					return render_template('Gestion_Personne.html',Login=Log)
					
			return redirect(url_for('Test_Compte'))	
		
		except Exception as e:
			print('erreur database: {}'.format(e))


		error = "Erreur-Affichage-Personne"
		return render_template("page_identification.html" , error=error)








	#
	@app.route('/Get_personne_update/<string:Login_data>',methods=['POST','GET'])
	def Get_personne_update(Login_data):
		
		try:

			global Log

			try:
				Log = Login_data

				if g.user:
					return redirect(url_for('Aff_Personne_update'))
				return redirect(url_for('Test_Compte'))	
	
			except Exception as e:
				print('erreur database: {}'.format(e))

			#return redirect(url_for('Persones'))

		except Exception as e:
			print('erreur database: {}'.format(e))

		error = "Erreur-Get-Personne"
		return render_template("page_identification.html" , error=error)



	#
	@app.route('/Aff_Personne_update',methods=['POST','GET'])
	def Aff_Personne_update():		

		try:
			
			#Session	
			if g.user:


				cur =conn.cursor()
				cur.execute("SELECT count(*) FROM Technicien ")
				data_Nb_Tech = cur.fetchall()
				Data_Nb_Tech=data_Nb_Tech
				
				for x in Data_Nb_Tech :
					print(x)
					for y in x:
						var1=y
				print("*********")
				print(var1)




				cur =conn.cursor()
				cur.execute("SELECT count(*) FROM Operateur ")
				data_Nb_O = cur.fetchall()
				Data_Nb_O=data_Nb_O
				
				for x in Data_Nb_O :
					print(x)
					for y in x:
						var2=y
				print("*********")
				print(var2)





				cur =conn.cursor()
				cur.execute("SELECT count(*) FROM Responsable ")
				data_Nb_R = cur.fetchall()
				Data_Nb_R=data_Nb_R
				
				for x in Data_Nb_R :
					print(x)
					for y in x:
						var3=y
				print("*********")
				print(var3)





				cur =conn.cursor()
				cur.execute("SELECT count(*) FROM super_responsable ")
				data_Nb_SR = cur.fetchall()
				Data_Nb_SR=data_Nb_SR
				
				for x in Data_Nb_SR :
					print(x)
					for y in x:
						var4=y
				print("*********")
				print(var4)

				
				cur =conn.cursor()

				donnees_T =  'SELECT * FROM Technicien'
				donnees_O =  'SELECT * FROM Operateur'
				donnees_R =  'SELECT * FROM Responsable'				

				data =cur.execute(donnees_T)
				data = cur.fetchone()

				while data is not None :

					if int(Log)== data[0] :

						cur.execute('SELECT * FROM Technicien WHERE Login_Technicien=%s', (Log))
						donnees_t_update = cur.fetchall()
						Data_t = donnees_t_update

					
						return render_template("update_personne.html", Login=session['user'],username=session['name'],select_Personne=donnees_t_update,personne="Technicien",var1=var1,var2=var2,var3=var3,var4=var4)

					else:
						data = cur.fetchone()
					


				data =cur.execute(donnees_O)
				data = cur.fetchone()

				while data is not None :

					if int(Log)== data[0] :
						cur.execute('SELECT * FROM Operateur WHERE Login_Operateur=%s', (Log))
						donnees_o_update = cur.fetchall()
						Data_o = donnees_o_update
						return render_template("update_personne.html", Login=session['user'],username=session['name'],select_Personne=Data_o,personne="Operateur",var1=var1,var2=var2,var3=var3,var4=var4)
					
					else:
						data = cur.fetchone()


				data =cur.execute(donnees_R)
				data = cur.fetchone()

				while data is not None :

					if int(Log)== data[0] :
						cur.execute('SELECT * FROM Responsable WHERE Login_Responsable=%s', (Log))
						donnees_o_update = cur.fetchall()
						Data_o = donnees_o_update
						return render_template("update_personne.html", Login=session['user'],username=session['name'],select_Personne=Data_o,personne="Responsable",var1=var1,var2=var2,var3=var3,var4=var4)
					
					else:
						data = cur.fetchone()


					
			return redirect(url_for('Test_Compte'))	
		
		except Exception as e:
			print('erreur database: {}'.format(e))


		error = "Erreur-Affichage-Personne"
		return render_template("page_identification.html" , error=error)



	@app.route('/Modifier_Personne',methods=['POST','GET'])
	def Modifier_Personne():

		try:
			
			global Log_utilisateur	
			global Data_select
			global login
			global mdp
			global nom
			global prenom
			global email
			global n_tel
			global code


			if request.method == 'POST':
				
				log=request.form['Login_utilisateur']
				data_select=request.form['data_select']
				L = request.form['Login']
				M= request.form['Mdp']
				N = request.form['Nom']
				P = request.form['Prenom']
				Em = request.form['email']
				N_T = request.form['N_Tel']
				C = request.form['Code']
							
				Log_utilisateur=log
				Data_select=data_select
				login=L
				mdp = M
				nom = N
				prenom = P
				em = Em
				#email = E
				n_tel = N_T
				code = C
				print(mdp)
				print(nom)
				print(prenom)
				print(em)
				print(n_tel)
				print(code)
				print(login)
				print(Log_utilisateur)
				#prenom(email)
				cur =conn.cursor()

				sql_t =  'SELECT * FROM Technicien'
				sql_o =  'SELECT * FROM Operateur'
				sql_r = 'SELECT * FROM Responsable'

				data = cur.execute(sql_t)
				data =cur.fetchone()
				print("**********888888888*************")
				
				
				

				while data is not None :

					if int(login)== data[0] :
						
						cur.execute("""
								  UPDATE Technicien
								  SET  Mdp=%s, Nom=%s, Prenom =%s, Email=%s, N_tel=%s, Nb_travail=%s,Login_Technicien=%s
								  WHERE Login_Technicien =%s"""
							, (mdp, nom, prenom, em, n_tel, code,login,login))

						conn.commit()

						#Session
						if g.user:
							flash("Technicien modifié avec succès")
							return redirect(url_for('Aff_Personne'))
						return redirect(url_for('Test_Compte'))	
						
					else:
						data = cur.fetchone()


				data = cur.execute(sql_o)
				data =cur.fetchone()


				while data is not None :

					if int(login)== data[0] :
						
						cur = conn.cursor()
						cur.execute("""
								  UPDATE Operateur
								  SET  Mdp=%s, Nom=%s, Prenom =%s, Email=%s, N_tel=%s, Nb_travail=%s,Login_Operateur=%s
								  WHERE Login_Operateur =%s"""
							, (mdp, nom, prenom, em, n_tel, code,login,login))

						conn.commit()

						#Session
						if g.user:
							flash("Operateur modifié avec succès")
							return redirect(url_for('Aff_Personne'))
						return redirect(url_for('Test_Compte'))	

					else:
						data = cur.fetchone()

				


				data = cur.execute(sql_r)
				data =cur.fetchone()


				while data is not None :

					if int(login)== data[0] :
						
						cur = conn.cursor()
						cur.execute("""
								  UPDATE Responsable
								  SET  Mdp=%s, Nom=%s, Prenom =%s, Email=%s, N_tel=%s, Nb_travail=%s,Login_Responsable=%s
								  WHERE Login_Responsable =%s"""
							, (mdp, nom, prenom, em, n_tel, code,login,login))

						conn.commit()

						#Session
						if g.user:
							flash("Responsable modifié avec succès")
							return redirect(url_for('Aff_Personne'))
						return redirect(url_for('Test_Compte'))	

					else:
						data = cur.fetchone()

				

		except Exception as e:
			print('erreur database: {}'.format(e))

		#Session
		if g.user:

			flash("Les données ne sont pas modifié")
			return redirect(url_for('Aff_Personne'))

		return redirect(url_for('Test_Compte'))	




	@app.route('/delete_Personne/<string:Log_data>', methods = ['GET'])
	def delete_Personne(Log_data):

		try:

			cur =conn.cursor()

			sql_T =  'SELECT * FROM Technicien'
			sql_O =  'SELECT * FROM Operateur'
			sql_R = 'SELECT * FROM Responsable'

			data = cur.execute(sql_T)
			data =cur.fetchone()

			while data is not None :

				if int(Log_data)== data[0] :
					
					cur = conn.cursor()
					cur.execute("DELETE FROM Technicien WHERE Login_Technicien=%s", (Log_data,))
					conn.commit()
					
					if g.user:
						flash("Technicien Supprimé avec succès")
						return redirect(url_for('Aff_Personne'))
					return redirect(url_for('Test_Compte'))	
					
				else:
					data = cur.fetchone()


			data = cur.execute(sql_O)
			data =cur.fetchone()

			while data is not None :

				if int(Log_data)== data[0] :

					cur = conn.cursor()
					cur.execute("DELETE FROM Operateur WHERE Login_Operateur=%s", (Log_data,))
					conn.commit()
					if g.user:
						flash("Operateur Supprimé avec succès")
						return redirect(url_for('Aff_Personne'))
					return redirect(url_for('Test_Compte'))	
				else:
					data = cur.fetchone()


			data = cur.execute(sql_R)
			data =cur.fetchone()

			while data is not None :

				if int(Log_data)== data[0] :

					cur = conn.cursor()
					cur.execute("DELETE FROM Responsable WHERE Login_Responsable=%s", (Log_data,))
					conn.commit()
					if g.user:
						flash("Responsable Supprimé avec succès")
						return redirect(url_for('Aff_Personne'))
					return redirect(url_for('Test_Compte'))	
				else:
					data = cur.fetchone()


		except Exception as e:
			print('erreur database: {}'.format(e))




	@app.route('/technicien_cest_partie',methods=['POST','GET'])
	def technicien_cest_partie():

		try:
			
			global Log_utilisateur	
			global id_n
			global M
			global s
			global d
			global eu
			global date

			if request.method == 'POST':
				

				id_n=request.form['id_notif']
				M = request.form['machine']
				s = request.form['secteur']
				d = request.form['description']
				eu = request.form['etat_u']
				date = request.form['date_interv']
				login = session['user']
				print(id_n)
				print(M)
				print(s)
				print(d)
				print(eu)
				print(date)
			
				cur =conn.cursor()

				sql_t =  'SELECT * FROM Technicien'
			
				data = cur.execute(sql_t)
				data =cur.fetchone()
				print("**********888888888*************")

				while data is not None :

					if int(login)== data[0] :
						nbTravail= data[6]+1
						cur.execute("""
								  UPDATE Technicien
								  SET   Nb_travail=%s
								  WHERE Login_Technicien =%s"""
							, (nbTravail,login))

						conn.commit()


						cur = conn.cursor()
						cur.execute("DELETE FROM notification_intervention_responsable_to_tevhnicien WHERE Id_Notification=%s", (id_n,))
						conn.commit()



						#Session
						if g.user:
							flash("Merci pour vos efforts")
							return redirect(url_for('page_liste_recoit_intervention'))
						return redirect(url_for('Test_Compte'))	
						
					else:
						data = cur.fetchone()


		except Exception as e:
			print('erreur database: {}'.format(e))

		#Session
		if g.user:

			flash("Les données ne sont pas modifié, erreur de c'est partie")
			return redirect(url_for('page_liste_recoit_intervention'))

		return redirect(url_for('Test_Compte'))	

