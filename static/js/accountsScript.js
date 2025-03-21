





document.getElementById("button2").addEventListener("click", function() {
  let usernameSpan = document.getElementById("username");
  let form = document.getElementById("adminUser-form")
  
  let input = document.createElement("input");
  input.type = "text";
  input.value = usernameSpan.textContent;
  input.name = "username"
  
  usernameSpan.replaceWith(input);
  input.focus(); 

  input.addEventListener("keypress", function(event) {
      if (event.key === "Enter") {
          let newUsername = input.value.trim(); 
          if (newUsername) {
              form.submit()
              let newSpan = document.createElement("span");
              newSpan.id = "username";
              newSpan.textContent = newUsername;
              input.replaceWith(newSpan);
          }
      }
  });

  
  input.addEventListener("blur", function() {
      let newUsername = input.value.trim();
      if (newUsername) {
          form.submit()
          let newSpan = document.createElement("span");
          newSpan.id = "username";
          newSpan.textContent = newUsername;
          input.replaceWith(newSpan);
      }
  });
});






document.getElementById("button3").addEventListener("click", function() {
  let firstnameSpan = document.getElementById("firstname");
  let form = document.getElementById("adminUser-form")
  
  let input = document.createElement("input");
  input.type = "text";
  input.value = firstnameSpan.textContent;
  input.name = "firstname"

  firstnameSpan.replaceWith(input);
  input.focus(); 

  
  input.addEventListener("keypress", function(event) {
      if (event.key === "Enter") {
          let newFirstname = input.value.trim(); 
          if (newFirstname) {
              form.submit()
              let newSpan = document.createElement("span");
              newSpan.id = "firstname";
              newSpan.textContent = newFirstname;
              input.replaceWith(newSpan);
          }
      }
  });

  
  input.addEventListener("blur", function() {
      let newFirstname = input.value.trim();
      if (newFirstname) {
          form.submit()
          let newSpan = document.createElement("span");
          newSpan.id = "firstname";
          newSpan.textContent = newFirstname;
          input.replaceWith(newSpan);
      }
  });
});





document.getElementById("button4").addEventListener("click", function() {
  let lastnameSpan = document.getElementById("lastname");
  let form = document.getElementById("adminUser-form")
  
  let input = document.createElement("input");
  input.type = "text";
  input.value = lastnameSpan.textContent;
  input.name = "lastname"

  lastnameSpan.replaceWith(input);
  input.focus(); 

 
  input.addEventListener("keypress", function(event) {
      if (event.key === "Enter") {
          let newLastname = input.value.trim(); 
          if (newLastname) {
              form.submit()
              let newSpan = document.createElement("span");
              newSpan.id = "lastname";
              newSpan.textContent = newLastname;
              input.replaceWith(newSpan);
          }
      }
  });


  input.addEventListener("blur", function() {
      let newLastname = input.value.trim();
      if (newLastname) {
          form.submit()
          let newSpan = document.createElement("span");
          newSpan.id = "lastname";
          newSpan.textContent = newLastname;
          input.replaceWith(newSpan);
      }
  });
});





document.getElementById("button5").addEventListener("click", function() {
  let emailSpan = document.getElementById("email");
  let form = document.getElementById("adminUser-form")
  
  let input = document.createElement("input");
  input.type = "text";
  input.value = emailSpan.textContent;
  input.name = "email"
  
  emailSpan.replaceWith(input);
  input.focus(); 

  input.addEventListener("keypress", function(event) {
      if (event.key === "Enter") {
          let newEmail = input.value.trim();
          if (newEmail) {
              form.submit()
              let newSpan = document.createElement("span");
              newSpan.id = "email";
              newSpan.textContent = newEmail;
              input.replaceWith(newSpan);
          }
      }
  });

  
  input.addEventListener("blur", function() {
      let newEmail = input.value.trim();
      if (newEmail) {
          form.submit()
          let newSpan = document.createElement("span");
          newSpan.id = "email";
          newSpan.textContent = newEmail;
          input.replaceWith(newSpan);
      }
  });
});





document.getElementById("button6").addEventListener("click", function() {
  let passwordSpan = document.getElementById("password");
  let form = document.getElementById("adminUser-form")
 
  let input = document.createElement("input");
  input.type = "text";
  input.value = passwordSpan.textContent;
  input.name = "password"
  
  passwordSpan.replaceWith(input);
  input.focus(); 

 
  input.addEventListener("keypress", function(event) {
      if (event.key === "Enter") {
          let newPassword = input.value.trim(); 
          if (newPassword) {
              form.submit()
              let newSpan = document.createElement("span");
              newSpan.id = "password";
              newSpan.textContent = newPassword;
              input.replaceWith(newSpan);
          }
      }
  });

 
  input.addEventListener("blur", function() {
      let newPassword = input.value.trim();
      if (newPassword) {
          form.submit()
          let newSpan = document.createElement("span");
          newSpan.id = "password";
          newSpan.textContent = newPassword;
          input.replaceWith(newSpan);
      }
  });
});


