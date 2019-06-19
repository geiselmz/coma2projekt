def print_tex(YT,boxl):
	"""
	Input: Young Tableau YT gegeben als Liste von Listen
	Output: -
	Funktion: Schreibt das Yoiun-Tableau als LaTeX-Code in die Datei
	visual.tex
	"""
	
	#Zunaechst leeren wir die Datei
	datei=open('visual.tex','w')
	datei.write('')
	datei.close
	
	#Nun fuegen wir das neue Young Tableau in die Datei ein
	#TODO: Boxlength
	datei=open('visual.tex','a')
	datei.write('\documentclass{article}\n')
	datei.write('\n')
	datei.write('\\')
	datei.write('usepackage{tikz}')
	datei.write('\\')
	datei.write('usetikzlibrary{calc}\n')
	datei.write('\\')
	datei.write('begin{document}\n')
	datei.write('\\')
	datei.write('begin{figure}\n')
	datei.write('\\')
	datei.write('tikzset{tick/.style={black,very thick}}\n')
	datei.write('\n')
	datei.write('\n')
	datei.write('\\')
	datei.write('begin{tikzpicture}\n') #hier bixlength beachten
	datei.write('\n')
	Zeilenzahl=0
	Kastenzahl=0
	for Zeile in YT:
		for Kasten in Zeile:
			datei.write('\draw[ultra thick](%s,%s) rectangle (%s,%s);\n' % (Kastenzahl,Zeilenzahl,Kastenzahl+1,Zeilenzahl+1))
			datei.write('\\')
			datei.write('node at ($((%s,%s)+(0.5,0.5)$) {$%s$};\n' % (Kastenzahl,Zeilenzahl,Kasten))
			Kastenzahl+=1
		Zeilenzahl+=1
		Kastenzahl=0
		datei.write('\n')
	datei.write('\end{tikzpicture}\n')
	datei.write('\n')
	datei.write('\end{figure}\n')
	datei.write('\end{document}\n')
	datei.close()
