function validation()
{

    var uname=document.getElementById("username").value;
        if (uname=="")
        {
            alert("Please enter your username.");
            return false;
        }
        if (uname.length<2)
        {
            alert("Please enter more then one charcter.");
            return false;
        }

        if (!isNaN(uname))
        {
            alert("Please write Only Alphabates.").value;
            return false;
        }

    var number=document.getElementById("mobile").value;
        if (number=="")
        {
            alert("Please enter your mobile number.");
            return false;
        }
        if (isNaN(number))
        {
            alert("Please write your currect number.");
            return false;
        }
        if (number.length<10 || number.length>10)
        {
            alert("Please write your 10 digit mobile number.");
            return false;
        }

    var email=document.getElementById("email").value;
        if (email=="")
        {
            alert("Please enter your Email.");
            return false;
        }
        if (email.indexOf('@')<=0 || email.charAt(email.length-10)!='@')
        {
            alert("Invalid posion of '@' ");
            return false;
        }
        if (email.charAt(email.length-4)!='.' && email.charAt(email.length-3)!='.')
        {
            alert("Invalid posion of '.' ");
            return false;
        }

    var password=document.getElementById("password").value;
        if (password=="")
        {
            alert("Please enter password.");
            return false;
        }
        if (password.length<8)
        {
            alert("Please enter atlist 8 characters.");
            return false;
        }
        if (password.search(/[0-9]/)==-1)
        {
            alert("Please add 1 numeric characters.");
            return false;
        }
        if (password.search(/[a-z]/)==-1)
        {
            alert("Please add lower case characters.");
            return false;
        }
        if (password.search(/[A-Z]/)==-1)
        {
            alert("Please add upper case characters.");
            return false;
        }
        if (password.search(/[!\@\#\$\%\^\&\*\(\)\?\-\+\*]/)==-1)
        {
            alert("Please add one special symbol.");
            return false;
        }

    var cpassword=document.getElementById("cpassword").value;
        if (cpassword!=password)
        {
            alert("Confirm Password dose not match to Password.");
            return false;
        }
        
}
