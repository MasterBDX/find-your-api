$(function(){
    
    // Url Validation ----------------------------
    const spinnerIcon = `
    <div style="">
        <i style="color:#29cd71" class="fas fa-sync fa-lg fa-pulse"></i>
    </div>
        `
    function validURL(str) {
        // check if string is valid url --------------        
        var pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
          '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
          '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
          '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
          '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
          '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
        return !!pattern.test(str);
      }
    

    //  update url-holder with exist input value --------------

    const url =   $('#try-api-input').val()
    if (url){
        if (validURL(url)){
            $('#url-holder').text(url)
        }
    }

    // Url Input Change event --------------

    $('#try-api-input').change(function(e){
        let errorMsg = `
                <div class="alert alert-warning alert-dismissible fade show " role="alert">        
                    Please enter a valid url
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
            `
        e.preventDefault();
        const value = $(this).val()
        const validation = validURL(value)
        if (validation){
            $('#error-msg').empty(errorMsg)
            $('#url-holder').text(value)
            $(this).val('')
        }
        else{
            $('#error-msg').html(errorMsg)
        }
    })

    // Run Script Btn click event --------------
    
    $('#run-btn').click(function(e){
        e.preventDefault();
        let jsonContainer = $('#json-holder')
        let url = $('#url-holder').text()
        jsonContainer.html(spinnerIcon)
        fetch(url)
        .then(response => response.json())
        .then(json => {
            jsonContainer.empty()
            jsonContainer.html(JSON.stringify(json, null, "  "))
            hljs.initHighlighting.called = false;
            hljs.initHighlighting();
            })
        .catch((error) => {
                console.error('Error:', error);
                jsonContainer.html(`
                    <div style="color:#ff5d5a">
                        ${error}                        
                    </div>
                `)
                        });
    })

    // Copy Btn Click Event
    function fallbackCopyTextToClipboard(e) {
        e.preventDefault()
        
        let text = $('#json-holder').text();
        var textArea = document.createElement("textarea");
        textArea.value = text;
        
        // Avoid scrolling to bottom
        textArea.style.top = "0";
        textArea.style.left = "0";
        textArea.style.position = "fixed";
      
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        try {
          var successful = document.execCommand('copy');
          var msg = successful ? 'successful' : 'unsuccessful';
          $(this).text('Copied')
            
        } catch (err) {
          console.error('Fallback: Oops, unable to copy', err);
        }  
        document.body.removeChild(textArea);
      }
      
        $('#copy-btn').click(fallbackCopyTextToClipboard)

      
       
        $('#clean-btn').click(function(e){
            e.preventDefault()
            $('#json-holder').text(`{}`)
            
            
        })


})
    
    

