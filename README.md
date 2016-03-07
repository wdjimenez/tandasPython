# tandasPython

* Referencias

   - Cómo instalar PyQt4 en Windows, Linux y Mac OS X
      + http://www.pythondiario.com/2013/11/como-instalar-pyqt4-en-windows-linux-y.html
         + https://www.riverbankcomputing.com/software/pyqt/download

* Comandos de Git que pueden servirte:

   - Ramas

      * $ git branch                // muestra las ramas creadas
      * $ git checkout -b prueba    // se crea una Nueva rama llamada prueba
      * $ git checkout master	      // hacemos el cambio a rama master
      * $ git branch                // muestra en qué rama estas trabajando
      * $ git merge prueba	         // mezclas ramas (master y prueba)

      * $ git status                // muestra los cambios realizados
      * $ python nombredelarchivoconconflictos       // aquí ya arreglas tus conflictos

      * $ git add -A                // agregas cambios
      * $ git commit -m "Mezclando la rama prueba" // haces el commit de tus cambios

   - Clonar Ramas

      * $ git clone -b name_branch http_clone_url_of_github

   - Conflictos con ramas

      * Cuando al dar git pull en consola y me marca que se ha creado una nueva rama debo crear la rama con:
         + $ git checkout -b nombreRama

 	   * y después dar el:
	      + $ git pull origin nombreRama

      * para así poder bajar los cambios.

      * Si estamos trabajando en nuestro código y necesitamos cambiar a otra rama o quizás hacer un pull al repositorio, y no quiero hacer un commit de mi trabajo, puedo usar:

         + $ git stash

         - lo que hace es congelar mis cambios desde mi último commit y almacenarlos en una pila de forma temporal dejando mi directorio de trabajo completamente limpio.

      * Ahora puedo: cambiar de rama, trabajar un rato, hacer un pull:
	     + $ git pull

      * después de realizar nuestro trabajo puedo volver a recuperar mis cambios:
         - con:
	        + $ git stash list              // puedo ver la lista de stashes

         - Puedo ver en qué consisten los cambios usando:
	        + $ git stash show stash@{#}	  //# es el número de stash

         - Puedes utilizar las herramientas de git sobre tu stash con:
	        + $ git diff stash@{#}

         - Y finalmente puedes aplicar los cambios del stash a tu directorio de trabajo con:
	        + $ git stash apply stash@{#}

         - Si solamente tienes un stash puedes utilizar tranquilamente
	        + $ git stash apply

         - ó
	        + $ git stash pop

         - Para eliminar todos los stashes almacenados lo hacemos con:
	        + $ git stash clear

      * para revertir un commit utilizamos:
         - $ git revert #codigo-commit
