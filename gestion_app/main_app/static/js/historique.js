var myArray = []
$(function($) {
    $.ajax({
        data: $(this).serialize(), // get the form data
        type: $(this).attr('GET'), // GET or POST
        url: "http://127.0.0.1:8000/historique/",
        success: function(response) {
            let historique = response.historique
            let reception = response.materielle_data
            let livraison = response.Livraison_data
            console.log('historique', historique)
            console.log('reception', reception)
            console.log('livraison', livraison)
            myArray = reception
            buildTable(myArray);



        }
    })
})

var myArray1 = []
$(function($) {
    $.ajax({
        data: $(this).serialize(), // get the form data
        type: $(this).attr('GET'), // GET or POST
        url: "http://127.0.0.1:8000/historique/",
        success: function(response) {
            let historique = response.historique
            let reception = response.materielle_data
            let livraison = response.Livraison_data
            console.log('historique', historique)
            console.log('reception', reception)
            console.log('livraison', livraison)
            myArray1 = livraison
            buildTable1(myArray1);



        }
    })
})

function buildTable(data) {
    let table = document.getElementById('myTable');

    for (var i = 0; i < data.length; i++) {
        var row = `<tr>
						<td>${data[i].Category_name}</td>
                        <td>${data[i].Designation_Object}</td>
						<td>${data[i].Date_reception.slice(0, 10)}</td>
                        <td>${data[i].Emplacement}</td>
                        <td>${data[i].Etat}</td>
                        <td>${data[i].Numero_inventaire_entre}</td>
                        <td>${data[i].Quantite}</td>
                        <td>${data[i].Observation}</td>
                        <td>${data[i].Prix_achat_total}</td>
                        <td>${data[i].Prix_achat_unite}</td>
                        <td>${data[i].Serie}</td>
                        <td>${data[i].author_reception}</td>
					  </tr>`
        table.innerHTML += row


    }
}

function buildTable1(data) {
    let table = document.getElementById('myTable2');

    for (var i = 0; i < data.length; i++) {
        console.log('test')
        var row = `<tr>
                        <td>${data[i].Titre_livraison}</td>
                        <td>${data[i].Date_sortie.slice(0, 10)}</td>
						<td>${data[i].Centre}</td>
                        <td>${data[i].Sous_centre_id}</td>
						<td>${data[i].Decompte}</td>
                        <td>${data[i].Numero_inventaire_sortie}</td>
                        <td>${data[i].Prix_unitaire}</td>
                        <td>${data[i].Quantite_livree}</td>
                        <td>${data[i].author_livraison}</td>
					  </tr>`
        table.innerHTML += row


    }
}