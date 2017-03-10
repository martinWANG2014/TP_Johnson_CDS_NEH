from tkinter import *
import numpy

####################
# parameter for graphic.
facteur_echelle = 10
delta = 50
deltaM = delta / 2
hauteur_rectangle = deltaM
intermachine = 2 * hauteur_rectangle


def design_machine(zone_dessin, horizon, p_ij, nbm):
    for j in range(0, nbm):
        posy = delta + intermachine * j
        zone_dessin.create_line(delta, posy, delta + horizon, posy)
        zone_dessin.create_text(deltaM, posy - hauteur_rectangle / 2, text='M' + str(j + 1))
    posy += intermachine / 2
    zone_dessin.create_line(delta, posy, delta + horizon, posy)
    for j in range(int(numpy.sum(p_ij))):
        posx = delta + j * facteur_echelle
        zone_dessin.create_line(posx, posy + 5, posx, posy - 5)
        if j % 5 == 0:
            zone_dessin.create_text(posx, posy + 10, text=str(j))


def design_task(zone_dessin, i, machine, debut, fin):
    milieu = (fin - debut) / 2
    posy = delta + intermachine * machine
    zone_dessin.create_rectangle(delta + debut * facteur_echelle,
                                 posy - hauteur_rectangle, delta + fin * facteur_echelle, posy)
    zone_dessin.create_text(delta + (debut + milieu) * facteur_echelle,
                            posy - hauteur_rectangle / 2, text=str(i + 1))


def graphic(title, seq, nbj, nbm, c_ij, p_ij):
    fenetre = Tk()
    horizon = numpy.sum(p_ij) * facteur_echelle
    Taille_fenetre_x = horizon + 4 * delta
    Taille_fenetre_y = (nbm + 1) * (intermachine)
    zone_dessin = Canvas(fenetre, width=Taille_fenetre_x, height=Taille_fenetre_y, bd=3)
    fenetre.title(title)
    zone_dessin.pack()
    design_machine(zone_dessin, horizon, p_ij, nbm)
    for j in range(nbj):
        jj = seq[j]
        for i in range(nbm):
            design_task(zone_dessin, jj, i, c_ij[i][j + 1] - p_ij[i][jj], c_ij[i][j + 1])
    fenetre.mainloop()
