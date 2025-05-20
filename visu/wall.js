
// Fonction pour créer un élément li avec les données spécifiées
function createListItem(artist, album, rgb, num) {
    // Création de l'élément li
    var listItem = document.createElement('li');

    // Création de l'élément img
    var img = document.createElement('img');
    img.src = '../im/im'+num+'.jpg';
    img.alt = 'Cover d\'album';
    listItem.appendChild(img);

    // Création de l'élément p pour l'artiste
    var artistPara = document.createElement('p');
    artistPara.className = 'artiste';
    artistPara.textContent = artist;
    listItem.appendChild(artistPara);

    // Création de l'élément p pour l'album
    var albumPara = document.createElement('p');
    albumPara.className = 'album';
    albumPara.textContent = album;
    listItem.appendChild(albumPara);

    // Conversion des valeurs RVB en chaîne pour la couleur de fond
    var rgbColor = 'rgb(' + rgb.join(',') + ')';
    listItem.style.backgroundColor = rgbColor;


    rgb = rgb.map(component => Math.round(component))

    // Création de l'élément p pour les valeurs RGB
    var rgbPara = document.createElement('p');
    rgbPara.className = 'rgb';
    rgbPara.textContent = '(' + rgb.join(',') + ')';
    listItem.appendChild(rgbPara);

    var teinte = 255- Math.max(rgb[0],rgb[1],rgb[2])
    listItem.style.color = 'rgb('+ teinte + ',' + teinte + ',' + teinte + ')' ;
    
    


    return listItem;
}



function miseEnPlace() {
    // Récupérer l'élément ul
    var ul = document.querySelector('ul');

    // Lire le fichier contenant les données
    fetch('../data.txt')
        .then(response => response.text())
        .then(data => {
            // Diviser les données en lignes
            var lines = data.split('\n');

            // Parcourir chaque ligne et créer les éléments li correspondants
            lines.forEach(line => {
                var [num, album, artist, rgb] = line.split('\t');

                // Convertir la chaîne RGB en tableau d'entiers
                rgb = rgb.slice(1, -1).split(',').map(Number);

                // Créer un nouvel élément li en utilisant les données de la ligne
                var newItem = createListItem(artist, album, rgb, num);

                // Ajouter l'élément li à la liste ul
                ul.appendChild(newItem);
            });
        });
}

window.addEventListener("load", miseEnPlace, false)
