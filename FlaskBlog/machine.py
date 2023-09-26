from flask import render_template, request, redirect, url_for ,flash, session, g
from FlaskBlog import conn

from FlaskBlog import app
from FlaskBlog import Compte


#classe 
class machine():

	def __init__(self, classes):
		self.machine = machine
		

	def GetMachine(self):
		return self.classes

	def SetMachine(self,machine):
		self.machine=machine



	


	# méthode 
	@app.route('/page_Ajouter_Machine/',methods=['POST','GET'])
	def page_Ajouter_Machine():
		try:
			
			#Session	
			if g.user:
 
					cur =conn.cursor()
					cur.execute("SELECT * FROM machine ")
					data_m = cur.fetchall()
					Data_MACHINE=data_m

			
					cur =conn.cursor()
					cur.execute("SELECT count(*) FROM machine ")
					data_Nb_M = cur.fetchall()
					Data_Nb_Machine=data_Nb_M

					var=0
					for x in Data_Nb_Machine :
						print(x)
						for y in x:
							var=y
					print("*********")
					print(var)


					return render_template('gestion_machine.html',Login=session['user'],username=session['name'],Machines=Data_MACHINE,Data_Nb_Machine=var)
					
			return redirect(url_for('Test_Compte'))	
		
		except Exception as e:
			print('erreur database: {}'.format(e))


		error = "Erreur-Affichage-Machine"
		return redirect(url_for('Test_Compte'))	








	#
	@app.route('/Get_machine_update/<string:M_data>',methods=['POST','GET'])
	def Get_machine_update(M_data):
		
		try:

			global dataM

			try:
				dataM = M_data

				if g.user:
					return redirect(url_for('Aff_Machine_update'))
				return redirect(url_for('Test_Compte'))	
	
			except Exception as e:
				print('erreur database: {}'.format(e))

			#

		except Exception as e:
			print('erreur database: {}'.format(e))

		error = "Erreur-Get-Machine"
		return render_template("page_identification.html" , error=error)



	#
	@app.route('/Aff_Machine_update',methods=['POST','GET'])
	def Aff_Machine_update():		

		try:
			
			#Session	
			if g.user:

				cur =conn.cursor()

				donnees_m =  'SELECT Nom_Machine FROM machine'

				data =cur.execute(donnees_m)
				data = cur.fetchone()

				while data is not None :

					if dataM == data[0] :

					
						DataM = data[0]

						return render_template("modifier_machine.html", Login=session['user'],username=session['name'],select_data_Machine=DataM)

					else:
						data = cur.fetchone()
					

					
			return redirect(url_for('Test_Compte'))	
		
		except Exception as e:
			print('erreur database: {}'.format(e))


		error = "Erreur-Affichage-Machine"
		return render_template("page_identification.html" , error=error)





	@app.route('/update_machine',methods=['POST','GET'])
	def update_machine():

		try:
			
			global Log_utilisateur	
			global Nom_utilisateur	

			global data_machine
			global new_data_machine


			if request.method == 'POST':
				
				
				new_M = request.form['nom_machine']
				machine_data_ancien = request.form['machine_data_ancien']
				data_machine = new_M
				
				print(new_M)
				print(machine_data_ancien)
				
				cur =conn.cursor()

				sql_machine =  'SELECT * FROM machine'

				data = cur.execute(sql_machine)
				data =cur.fetchone()				
				

				while data is not None :

					if machine_data_ancien == data[0] :
						
						if g.user:
							Log_utilisateur=session['user']
							#Nom_utilisateur=session['name']

							cur.execute("""
									  UPDATE machine
									  SET  Nom_Machine=%s
									  WHERE Nom_Machine =%s"""
								, (data_machine,machine_data_ancien))

							conn.commit()

							flash("Machine modifié avec succès")
							return redirect(url_for('page_Ajouter_Machine'))
						
						return redirect(url_for('Test_Compte'))	
						
					else:
						data = cur.fetchone()


		except Exception as e:
			print('erreur database: {}'.format(e))

		#Session
		if g.user:

			flash("Les données ne sont pas modifié")
			return redirect(url_for('page_Ajouter_Machine'))

		return redirect(url_for('Test_Compte'))	






	@app.route('/delete_Machine/<string:M_data>', methods = ['GET'])
	def delete_Machine(M_data):

		try:

			cur =conn.cursor()

			sql_Machine = 'SELECT * FROM machine'

			data = cur.execute(sql_Machine)
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
					cur.execute("DELETE FROM machine WHERE Nom_Machine=%s", (M_data,))
					conn.commit()
					
					if g.user:
						flash("Machine Supprimé avec succès")
						return redirect(url_for('page_Ajouter_Machine'))
					return redirect(url_for('Test_Compte'))	
					
				else:
					data = cur.fetchone()

		except Exception as e:
			print('erreur database: {}'.format(e))
			#return redirect(url_for('page_Ajouter_Classe'))





	# méthode 
	@app.route('/Ajouter_Machine/',methods=['POST','GET'])
	def Ajouter_Machine():

		try:

			global Log_utilisateur	
			global Nom_utilisateur	
			
			if g.user:
				Log_utilisateur=session['user']
				Nom_utilisateur=session['name']

				if request.method == 'POST':
										
					M = request.form['machine']


					try:
						cur = conn.cursor()
						cur.execute("INSERT INTO machine VALUES (%s,%s)", (M,Log_utilisateur ))
						conn.commit()
						flash("Machine Enregistré avec succès")
						return redirect(url_for('page_Ajouter_Machine'))	

					except Exception as e:
					
						flash("Machine "+ M +" existe déjà")
						return redirect(url_for('page_Ajouter_Machine'))	



			return redirect(url_for('Test_Compte'))	

		except Exception as e:
			print('erreur database: {}'.format(e))

		flash("Vérifier votre données")
		return render_template("page_Accueil_Admin.html", Login=Log_utilisateur,username=Nom_utilisateur)







