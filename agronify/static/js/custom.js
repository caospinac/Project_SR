$(function() {
                
    // Navigation scrolls
    $('.navbar-nav li a').bind('click', function(event) {
        $('.navbar-nav li').removeClass('active');
        $(this).closest('li').addClass('active');
        var $anchor = $(this);
        var nav = $($anchor.attr('href'));
        if (nav.length) {
        $('html, body').stop().animate({				
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        
        event.preventDefault();
        }
    });
    
    // Add smooth scrolling to all links in navbar
    $(".navbar a, a.mouse-hover, .overlay-detail a").on('click', function(event) {
        event.preventDefault();
        var hash = this.hash;
        $('html, body').animate({
            scrollTop: $(hash).offset().top
        }, 900, function(){
            window.location.hash = hash;
        });
    });

    $('#loginForm').submit(function(e) {
        e.preventDefault();
        var formdata = $(this).serializeArray();
        console.log(formdata);
        d = $.ajax({
            url: "/api/sign-in",
            type: 'POST',
            dataType: 'application/json',
            data: formdata

        });

        $(location).attr('href', '/home')
       

    });

    $('#registerForm').submit(function(e) {
        e.preventDefault();
        var formdata = $(this).serializeArray();
        console.log(formdata);
        $.ajax({
            url: "/api/users",
            type: 'POST',
            dataType: 'application/json',
            data: formdata,
            success: function(data)
            {
                
            }

        });
       

    });


    $('#registerForm').validate({
        rules:
        {
            firstname: {
                required: true,
                minlength: 3,
                maxlength: 40
            },
            lastname: {
                required: true,
                minlength: 2,
                maxlength: 40
            },
             password: {
                required: true,
                minlength: 6,
                maxlength: 20
            },
            password2: {
                required: true,
                equalTo: '#pwd'
            },
            email: {
                required: true,
                email: true
            },
        },
        messages:
        {
            name: "Enter a valid name",
            lastname: "Enter a valid lastname",
            uname: "Enter a valid username",
            pwd:{
                required: "Provide a password",
                minlength: "Password needs to be minimum of 6 characters"
            },
            email: "Enter a valid email",
            pwd_again:{
                required: "Retype your password",
                equalTo: "Password mismatch! Retype"
            }
        },
        submitHandler: $(this).submit()
    });

    $.validator.setDefaults({
        highlight: function(element) {
            $(element).closest('.form-group').addClass('has-error');
        },
        unhighlight: function(element) {
            $(element).closest('.form-group').removeClass('has-error');
        },
        errorElement: 'span',
        errorClass: 'help-block',
        errorPlacement: function(error, element) {
            if(element.parent('.form-group').length) {
                error.insertAfter(element.parent());
            } else {
                error.insertAfter(element);
            }
        }
    });

    $('#singOutUser').click(function(e) {
        e.preventDefault();

        $.post('/api/sign-out');

        $(location).attr('href', '/');
       
        return false;

    });


});