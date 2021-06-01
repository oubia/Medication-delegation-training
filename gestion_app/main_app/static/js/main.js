$(function($) {
    $.ajax({
        data: $(this).serialize(), // get the form data
        type: $(this).attr('GET'), // GET or POST
        url: "http://127.0.0.1:8000/livraison/",
        // on success
        success: function(response) {
            const Centre_select = document.getElementById('Centre_select')
            const Sous_Centre = document.getElementById('Sous_Centre')

            let centre = response.centre
            let sous_centre = response.sous_centre

            for (i = 0; i < centre.length; i++) {
                let opt = document.createElement('option')
                opt.value = centre[i]['Centre_titre']
                opt.innerHTML = `${centre[i]['Centre_titre']}`
                document.getElementById('Centre_select').appendChild(opt)
            }

            function centre_selected() {
                let center_options = Centre_select.options[Centre_select.selectedIndex].text;
                let Centre_list = ['0']
                Centre_list.push(center_options)
                slected_value = String($(Centre_list).get(-1));
                select_file = Object.assign(slected_value)
                let sous_centre_data = []
                for (i = 0; i < centre.length; i++) {
                    if (centre[i]['Centre_titre'] == select_file) {
                        let id = centre[i]['id']
                        for (j = 0; j < sous_centre.length; j++) {
                            if (sous_centre[j]['centre_titre'] == id)
                                sous_centre_data.push(sous_centre[j]['Sous_centre_titre'])
                        }
                    }
                }
                Sous_Centre.length = 0
                for (i = 0; i < sous_centre_data.length; i++) {
                    let opt = document.createElement('option')
                    opt.value = sous_centre_data[i]
                    opt.innerHTML = `${sous_centre_data[i]}`
                    Sous_Centre.appendChild(opt)
                }
            }
            Centre_select.addEventListener('click', centre_selected, false)
        },
        // on error
        error: function(response) {
            // alert the error if any error occured
            alert(response.responseJSON.errors);
            console.log(response.responseJSON.errors)
        }
    });
    return false;

})