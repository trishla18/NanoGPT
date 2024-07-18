var configurableURL = "http://localhost:5087"; //Change this
if(sessionStorage.getItem("userMail")!=null)
{
  window.location = "subjects.html";
}
function hashcode(str)
{
  var hash = 0,i, chr;
  if (str.length === 0) return hash;
  for (i = 0; i < str.length; i++)
  {
    chr = str.charCodeAt(i);
    hash = ((hash << 5) - hash) + chr;
    hash |= 0;
  }
  return hash;
}
function login(e)
{
    e.preventDefault();
    var username = document.getElementById("username").value.toLowerCase();
    var password = document.getElementById("password").value;
    if(username.length!=0 && password.length!=0)
    {
      var pwd_pattern = /^[a-zA-Z0-9#]{8,}$/;
      var result = password.match(pwd_pattern);
      if(result)
      {
        window.location = "subjects.html"; //Remove this after integration
        return;
        $.get({
          url: configurableURL+"<apiurl>",
          data: {"email":username,"password":hashcode(password).toString()},
          success: function(response){
            if(response.flag==="1")
            {
              window.sessionStorage.setItem("userMail", username);
              window.sessionStorage.setItem("userName", response.name);
              window.location = "subjects.html";
            }
            else if(response.flag==="0")
            {
              alert("Incorrect username/password");
            }
            else
            {
              console.log(response.error);
            }
          },
          dataType: "json"
        });
      }
      else
      {
        alert("Invalid Password!");
        return;
      }
    }
    else if(username.length===0)
    {
      alert("Enter the username!");
      return;
    }
    else
    {
      alert("Enter the password");
      return;
    }
}