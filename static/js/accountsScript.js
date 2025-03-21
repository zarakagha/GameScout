



document.getElementById("button1").addEventListener("click", function() {
    let usernameSpan = document.getElementById("identity");

    // Create an input field and set its value to the current username
    let input = document.createElement("input");
    input.type = "text";
    input.value = usernameSpan.textContent;

    // Replace the current username with the input field
    usernameSpan.replaceWith(input);
    input.focus(); // Focus on the input field for immediate editing

    // When Enter is pressed, update the username
    input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            let newUsername = input.value.trim(); // Get new username
            if (newUsername) {
                let newSpan = document.createElement("span");
                newSpan.id = "identity";
                newSpan.textContent = newUsername;
                input.replaceWith(newSpan);
            }
        }
    });

    // Optional: If the user clicks outside, it also updates the username
    input.addEventListener("blur", function() {
        let newUsername = input.value.trim();
        if (newUsername) {
            let newSpan = document.createElement("span");
            newSpan.id = "identity";
            newSpan.textContent = newUsername;
            input.replaceWith(newSpan);
        }
    });
});






document.getElementById("button2").addEventListener("click", function() {
  let usernameSpan = document.getElementById("username");

  // Create an input field and set its value to the current username
  let input = document.createElement("input");
  input.type = "text";
  input.value = usernameSpan.textContent;

  // Replace the current username with the input field
  usernameSpan.replaceWith(input);
  input.focus(); // Focus on the input field for immediate editing

  // When Enter is pressed, update the username
  input.addEventListener("keypress", function(event) {
      if (event.key === "Enter") {
          let newUsername = input.value.trim(); // Get new username
          if (newUsername) {
              let newSpan = document.createElement("span");
              newSpan.id = "username";
              newSpan.textContent = newUsername;
              input.replaceWith(newSpan);
          }
      }
  });

  // Optional: If the user clicks outside, it also updates the username
  input.addEventListener("blur", function() {
      let newUsername = input.value.trim();
      if (newUsername) {
          let newSpan = document.createElement("span");
          newSpan.id = "username";
          newSpan.textContent = newUsername;
          input.replaceWith(newSpan);
      }
  });
});






document.getElementById("button3").addEventListener("click", function() {
  let usernameSpan = document.getElementById("firstname");

  // Create an input field and set its value to the current username
  let input = document.createElement("input");
  input.type = "text";
  input.value = usernameSpan.textContent;

  // Replace the current username with the input field
  usernameSpan.replaceWith(input);
  input.focus(); // Focus on the input field for immediate editing

  // When Enter is pressed, update the username
  input.addEventListener("keypress", function(event) {
      if (event.key === "Enter") {
          let newUsername = input.value.trim(); // Get new username
          if (newUsername) {
              let newSpan = document.createElement("span");
              newSpan.id = "firstname";
              newSpan.textContent = newUsername;
              input.replaceWith(newSpan);
          }
      }
  });

  // Optional: If the user clicks outside, it also updates the username
  input.addEventListener("blur", function() {
      let newUsername = input.value.trim();
      if (newUsername) {
          let newSpan = document.createElement("span");
          newSpan.id = "firstname";
          newSpan.textContent = newUsername;
          input.replaceWith(newSpan);
      }
  });
});





document.getElementById("button4").addEventListener("click", function() {
  let usernameSpan = document.getElementById("lastname");

  // Create an input field and set its value to the current username
  let input = document.createElement("input");
  input.type = "text";
  input.value = usernameSpan.textContent;

  // Replace the current username with the input field
  usernameSpan.replaceWith(input);
  input.focus(); // Focus on the input field for immediate editing

  // When Enter is pressed, update the username
  input.addEventListener("keypress", function(event) {
      if (event.key === "Enter") {
          let newUsername = input.value.trim(); // Get new username
          if (newUsername) {
              let newSpan = document.createElement("span");
              newSpan.id = "lastname";
              newSpan.textContent = newUsername;
              input.replaceWith(newSpan);
          }
      }
  });

  // Optional: If the user clicks outside, it also updates the username
  input.addEventListener("blur", function() {
      let newUsername = input.value.trim();
      if (newUsername) {
          let newSpan = document.createElement("span");
          newSpan.id = "lastname";
          newSpan.textContent = newUsername;
          input.replaceWith(newSpan);
      }
  });
});





document.getElementById("button5").addEventListener("click", function() {
  let usernameSpan = document.getElementById("email");

  // Create an input field and set its value to the current username
  let input = document.createElement("input");
  input.type = "text";
  input.value = usernameSpan.textContent;

  // Replace the current username with the input field
  usernameSpan.replaceWith(input);
  input.focus(); // Focus on the input field for immediate editing

  // When Enter is pressed, update the username
  input.addEventListener("keypress", function(event) {
      if (event.key === "Enter") {
          let newUsername = input.value.trim(); // Get new username
          if (newUsername) {
              let newSpan = document.createElement("span");
              newSpan.id = "email";
              newSpan.textContent = newUsername;
              input.replaceWith(newSpan);
          }
      }
  });

  // Optional: If the user clicks outside, it also updates the username
  input.addEventListener("blur", function() {
      let newUsername = input.value.trim();
      if (newUsername) {
          let newSpan = document.createElement("span");
          newSpan.id = "email";
          newSpan.textContent = newUsername;
          input.replaceWith(newSpan);
      }
  });
});





document.getElementById("button6").addEventListener("click", function() {
  let usernameSpan = document.getElementById("password");

  // Create an input field and set its value to the current username
  let input = document.createElement("input");
  input.type = "text";
  input.value = usernameSpan.textContent;

  // Replace the current username with the input field
  usernameSpan.replaceWith(input);
  input.focus(); // Focus on the input field for immediate editing

  // When Enter is pressed, update the username
  input.addEventListener("keypress", function(event) {
      if (event.key === "Enter") {
          let newUsername = input.value.trim(); // Get new username
          if (newUsername) {
              let newSpan = document.createElement("span");
              newSpan.id = "password";
              newSpan.textContent = newUsername;
              input.replaceWith(newSpan);
          }
      }
  });

  // Optional: If the user clicks outside, it also updates the username
  input.addEventListener("blur", function() {
      let newUsername = input.value.trim();
      if (newUsername) {
          let newSpan = document.createElement("span");
          newSpan.id = "password";
          newSpan.textContent = newUsername;
          input.replaceWith(newSpan);
      }
  });
});


