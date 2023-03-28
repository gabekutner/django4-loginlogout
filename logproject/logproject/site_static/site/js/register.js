var form_fields = document.getElementsByTagName('input')
        form_fields[1].placeholder = "Enter Your Username";
        form_fields[2].placeholder = "Enter Your Email";
        form_fields[3].placeholder = "Enter Your Password";
        form_fields[4].placeholder = "Confirm Your Password";

        for (var field in form_fields){
            form_fields[field].className += 'form-control'
        }