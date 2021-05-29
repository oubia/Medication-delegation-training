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
            myArray1 = livraison
            buildTable(myArray)
            buildTable1(myArray1)


        }
    })
})


function buildTable(data) {
    var table = document.getElementById('myTable')

    for (var i = 0; i < data.length; i++) {
        var row = `<tr>
						<td scope="row">${data[i].Category_name}</td>
                        <td scope="row">${data[i].Designation_Object}</td>
						<td scope="row">${data[i].Date_reception}</td>
                        <td scope="row">${data[i].Emplacement}</td>
                        <td scope="row">${data[i].Etat}</td>
                        <td scope="row">${data[i].Numero_inventaire_entre}</td>
                        <td scope="row">${data[i].Quantite}</td>
                        <td scope="row">${data[i].Observation}</td>
                        <td scope="row">${data[i].Prix_achat_total}</td>
                        <td scope="row">${data[i].Prix_achat_unite}</td>
                        <td scope="row">${data[i].Serie}</td>
                        <td scope="row">${data[i].author_reception}</td>
					  </tr>`
        table.innerHTML += row


    }
}

function buildTable1(data) {
    var table = document.getElementById('myTable2')

    for (var i = 0; i < data.length; i++) {
        var row = `<tr>
                        <td scope="row">${data[i].Titre_livraison}</td>
                        <td scope="row">${data[i].Date_sortie}</td>
						<td scope="row">${data[i].Centre}</td>
						<td scope="row">${data[i].Decompte}</td>
                        <td scope="row">${data[i].Numero_inventaire_sortie}</td>
                        <td scope="row">${data[i].Prix_unitaire}</td>
                        <td scope="row">${data[i].Numero_inventaire_entre}</td>
                        <td scope="row">${data[i].Quantite_livree}</td>
                        <td scope="row">${data[i].Observation}</td>
                        <td scope="row">${data[i].author_livraison}</td>
					  </tr>`
        table.innerHTML += row


    }
}