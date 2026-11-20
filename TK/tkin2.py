import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

window = tk.Tk()
window.geometry("1120x660")
window.title("Formulaire d'Inscription - Université de Boumerdes")
window.minsize(width=1120, height=660)
window.config(bg="#eef2f6")

style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox", fieldbackground="#f8fafc", background="#e2e8f0", bordercolor="#cbd5e1", arrowcolor="#1e3a8a", padding=5)
style.configure("Treeview", background="#f8fafc", fieldbackground="#f8fafc", foreground="#0f172a", rowheight=26, font=("Segoe UI", 9))
style.configure("Treeview.Heading", background="#1e3a8a", foreground="white", font=("Segoe UI", 9, "bold"))

header_frame = tk.Frame(window, bg="#1e3a8a", height=100)
header_frame.pack(fill="x")

uni_logo = tk.PhotoImage(file=r"C:\Users\user\Desktop\TP info\TK\uni_logo.png").subsample(5, 5)
uni_logo_canvas = tk.Canvas(header_frame, width=80, height=80, bg="white", highlightthickness=0)
uni_logo_canvas.place(x=25, y=10)
uni_logo_canvas.create_image(40, 40, image=uni_logo)

header = tk.Label(header_frame, text="Ministère de l'Enseignement Supérieur et de la Recherche Scientifique\nUniversité M'hamed BOUGARA BOUMERDES\nFaculté de Technologie", bg="#1e3a8a", fg="white", font=("Segoe UI", 11, "bold"), justify="center")
header.place(relx=0.5, y=50, anchor="center")

fac_logo = tk.PhotoImage(file=r"C:\Users\user\Desktop\TP info\TK\logo_fac.png").subsample(5, 5)
fac_logo_canvas = tk.Canvas(header_frame, width=80, height=80, bg="white", highlightthickness=0)
fac_logo_canvas.place(x=1015, y=10)
fac_logo_canvas.create_image(40, 40, image=fac_logo)

card_frame = tk.Frame(window, bg="white", highlightbackground="#cbd5e1", highlightthickness=1)
card_frame.place(x=20, y=118, width=650, height=465)

student_img = None

photo_frame = tk.LabelFrame(card_frame, text=" Photo Étudiant ", bg="white", fg="#1e3a8a", font=("Segoe UI", 9, "bold"), bd=1, relief="groove")
photo_frame.place(x=465, y=20, width=165, height=205)

photo_canvas = tk.Canvas(photo_frame, width=110, height=130, bg="#f1f5f9", highlightthickness=1, highlightbackground="#cbd5e1")
photo_canvas.place(x=25, y=8)
photo_canvas.create_text(55, 65, text="Photo", fill="#64748b", font=("Segoe UI", 9))

def parcourir_photo():
    global student_img
    filepath = filedialog.askopenfilename(title="Choisir une photo", filetypes=[("Images PNG/GIF", "*.png *.gif")])
    if filepath:
        img = tk.PhotoImage(file=filepath)
        facteur = max(1, img.width() // 110, img.height() // 130)
        student_img = img.subsample(facteur, facteur)
        photo_canvas.delete("all")
        photo_canvas.create_image(55, 65, image=student_img)

def ajouter_survol(bouton, couleur_normale, couleur_survol):
    bouton.bind("<Enter>", lambda e: bouton.config(bg=couleur_survol))
    bouton.bind("<Leave>", lambda e: bouton.config(bg=couleur_normale))

btn_photo = tk.Button(photo_frame, text="Parcourir...", command=parcourir_photo, bg="#3b82f6", fg="white", activebackground="#2563eb", activeforeground="white", font=("Segoe UI", 9, "bold"), relief="flat", cursor="hand2", width=14)
btn_photo.place(x=25, y=148)
ajouter_survol(btn_photo, "#3b82f6", "#2563eb")

lbl_nom = tk.Label(card_frame, text="Nom :", bg="white", fg="#334155", font=("Segoe UI", 10, "bold"))
lbl_nom.place(x=20, y=25)
ent_nom = tk.Entry(card_frame, width=28, font=("Segoe UI", 10), bg="#f8fafc", fg="#0f172a", relief="flat", highlightthickness=1, highlightbackground="#cbd5e1", highlightcolor="#2563eb")
ent_nom.place(x=175, y=25, height=28)

lbl_prenom = tk.Label(card_frame, text="Prénom :", bg="white", fg="#334155", font=("Segoe UI", 10, "bold"))
lbl_prenom.place(x=20, y=68)
ent_prenom = tk.Entry(card_frame, width=28, font=("Segoe UI", 10), bg="#f8fafc", fg="#0f172a", relief="flat", highlightthickness=1, highlightbackground="#cbd5e1", highlightcolor="#2563eb")
ent_prenom.place(x=175, y=68, height=28)

lbl_sexe = tk.Label(card_frame, text="Sexe :", bg="white", fg="#334155", font=("Segoe UI", 10, "bold"))
lbl_sexe.place(x=20, y=111)
var_sexe = tk.StringVar(value="Homme")
rad_homme = tk.Radiobutton(card_frame, text="Homme", variable=var_sexe, value="Homme", bg="white", fg="#334155", selectcolor="#eff6ff", activebackground="white", font=("Segoe UI", 10), cursor="hand2")
rad_homme.place(x=175, y=111)
rad_femme = tk.Radiobutton(card_frame, text="Femme", variable=var_sexe, value="Femme", bg="white", fg="#334155", selectcolor="#eff6ff", activebackground="white", font=("Segoe UI", 10), cursor="hand2")
rad_femme.place(x=265, y=111)

lbl_date = tk.Label(card_frame, text="Date de naissance :", bg="white", fg="#334155", font=("Segoe UI", 10, "bold"))
lbl_date.place(x=20, y=154)
ent_date = tk.Entry(card_frame, width=28, font=("Segoe UI", 10), bg="#f8fafc", fg="#0f172a", relief="flat", highlightthickness=1, highlightbackground="#cbd5e1", highlightcolor="#2563eb")
ent_date.place(x=175, y=154, height=28)

lbl_carte = tk.Label(card_frame, text="Num carte étudiant :", bg="white", fg="#334155", font=("Segoe UI", 10, "bold"))
lbl_carte.place(x=20, y=197)
ent_carte = tk.Entry(card_frame, width=28, font=("Segoe UI", 10), bg="#f8fafc", fg="#0f172a", relief="flat", highlightthickness=1, highlightbackground="#cbd5e1", highlightcolor="#2563eb")
ent_carte.place(x=175, y=197, height=28)

lbl_niveau = tk.Label(card_frame, text="Niveau :", bg="white", fg="#334155", font=("Segoe UI", 10, "bold"))
lbl_niveau.place(x=20, y=240)
combo_niveau = ttk.Combobox(card_frame, values=["L1", "L2", "L3"], width=26, state="readonly", font=("Segoe UI", 10))
combo_niveau.place(x=175, y=240)

lbl_annee = tk.Label(card_frame, text="Année universitaire :", bg="white", fg="#334155", font=("Segoe UI", 10, "bold"))
lbl_annee.place(x=20, y=283)
spin_annee = tk.Spinbox(card_frame, from_=2024, to=2030, width=27, font=("Segoe UI", 10), bg="#f8fafc", fg="#0f172a", relief="flat", highlightthickness=1, highlightbackground="#cbd5e1", highlightcolor="#2563eb")
spin_annee.delete(0, "end")
spin_annee.insert(0, "2026")
spin_annee.place(x=175, y=283, height=28)

lbl_mail = tk.Label(card_frame, text="Adresse mail :", bg="white", fg="#334155", font=("Segoe UI", 10, "bold"))
lbl_mail.place(x=20, y=326)
ent_mail = tk.Entry(card_frame, width=28, font=("Segoe UI", 10), bg="#f8fafc", fg="#0f172a", relief="flat", highlightthickness=1, highlightbackground="#cbd5e1", highlightcolor="#2563eb")
ent_mail.place(x=175, y=326, height=28)

lbl_adresse = tk.Label(card_frame, text="Adresse complète :", bg="white", fg="#334155", font=("Segoe UI", 10, "bold"))
lbl_adresse.place(x=20, y=369)
txt_adresse = tk.Text(card_frame, width=28, height=3, font=("Segoe UI", 10), bg="#f8fafc", fg="#0f172a", relief="flat", highlightthickness=1, highlightbackground="#cbd5e1", highlightcolor="#2563eb")
txt_adresse.place(x=175, y=369)

list_frame = tk.Frame(window, bg="white", highlightbackground="#cbd5e1", highlightthickness=1)
list_frame.place(x=685, y=118, width=415, height=465)

lbl_liste = tk.Label(list_frame, text="Liste des Étudiants Inscrits", bg="white", fg="#1e3a8a", font=("Segoe UI", 11, "bold"))
lbl_liste.place(x=15, y=10)

colonnes = ("nom", "prenom", "sexe", "naissance", "carte", "niveau", "annee", "mail", "adresse")
tree_etudiants = ttk.Treeview(list_frame, columns=colonnes, show="headings")

entetes = [("nom", "Nom", 85), ("prenom", "Prénom", 85), ("sexe", "Sexe", 60), ("naissance", "Naissance", 85), ("carte", "N° Carte", 90), ("niveau", "Niveau", 55), ("annee", "Année", 55), ("mail", "Email", 130), ("adresse", "Adresse", 150)]
for col, texte, largeur in entetes:
    tree_etudiants.heading(col, text=texte)
    tree_etudiants.column(col, width=largeur, anchor="center")

scrollbar_y = tk.Scrollbar(list_frame, orient="vertical", command=tree_etudiants.yview)
scrollbar_x = tk.Scrollbar(list_frame, orient="horizontal", command=tree_etudiants.xview)
tree_etudiants.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

tree_etudiants.place(x=15, y=42, width=368, height=390)
scrollbar_y.place(x=383, y=42, width=16, height=390)
scrollbar_x.place(x=15, y=432, width=368, height=16)

def reinitialiser_formulaire():
    global student_img
    ent_nom.delete(0, "end")
    ent_prenom.delete(0, "end")
    var_sexe.set("Homme")
    ent_date.delete(0, "end")
    ent_carte.delete(0, "end")
    combo_niveau.set("")
    spin_annee.delete(0, "end")
    spin_annee.insert(0, "2026")
    ent_mail.delete(0, "end")
    txt_adresse.delete("1.0", "end")
    student_img = None
    photo_canvas.delete("all")
    photo_canvas.create_text(55, 65, text="Photo", fill="#64748b", font=("Segoe UI", 9))

def valider_formulaire():
    if not ent_nom.get() or not ent_prenom.get() or not ent_carte.get() or not combo_niveau.get():
        messagebox.showwarning("Champs manquants", "Veuillez remplir les champs obligatoires (Nom, Prénom, Carte, Niveau) !")
    else:
        tree_etudiants.insert("", "end", values=(ent_nom.get(), ent_prenom.get(), var_sexe.get(), ent_date.get(), ent_carte.get(), combo_niveau.get(), spin_annee.get(), ent_mail.get(), txt_adresse.get("1.0", "end-1c")))
        messagebox.showinfo("Validation", f"Inscription validée et enregistrée pour {ent_nom.get()} {ent_prenom.get()} !")
        reinitialiser_formulaire()

def sauvegarder_fichier():
    lignes = tree_etudiants.get_children()
    if not lignes:
        messagebox.showwarning("Liste vide", "Aucun étudiant inscrit à enregistrer !")
        return
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichier texte", "*.txt")], title="Enregistrer la liste des étudiants")
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("Nom | Prénom | Sexe | Naissance | N° Carte | Niveau | Année | Email | Adresse\n")
            f.write("-" * 80 + "\n")
            for item in lignes:
                valeurs = tree_etudiants.item(item)["values"]
                f.write(" | ".join(str(v) for v in valeurs) + "\n")
        messagebox.showinfo("Sauvegarde réussie", "La liste des étudiants a été enregistrée avec succès !")

btn_valider = tk.Button(window, text="Valider l'inscription", command=valider_formulaire, bg="#10b981", fg="white", activebackground="#059669", activeforeground="white", font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", width=18)
btn_valider.place(x=140, y=598, height=36)
ajouter_survol(btn_valider, "#10b981", "#059669")

btn_reset = tk.Button(window, text="Réinitialiser", command=reinitialiser_formulaire, bg="#ef4444", fg="white", activebackground="#dc2626", activeforeground="white", font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", width=18)
btn_reset.place(x=340, y=598, height=36)
ajouter_survol(btn_reset, "#ef4444", "#dc2626")

btn_sauvegarder = tk.Button(window, text="Enregistrer la liste (.txt)", command=sauvegarder_fichier, bg="#1e3a8a", fg="white", activebackground="#172554", activeforeground="white", font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", width=22)
btn_sauvegarder.place(x=790, y=598, height=36)
ajouter_survol(btn_sauvegarder, "#1e3a8a", "#172554")

window.mainloop()
