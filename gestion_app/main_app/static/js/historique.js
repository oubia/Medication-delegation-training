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
        }
    })
})