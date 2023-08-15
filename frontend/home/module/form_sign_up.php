<div class="container">
  <div class="row d-flex justify-content-center align-items-center" style="min-height: 100vh;">
    <div class="col-md-12 p-5" id="sign_up_container">
      <div class="col-md-12 p-3">
        <h2 style="color: white;" class="p-2">Sign Up</h2>
      </div>
      <div class="col-md-6 float-left">
          <div class="form-group">
            <label for="user_name" style="color: white;">User name</label><br>
            <input type="text" class="w-100 p-1" id="user_name">
          </div>
          <div class="form-group p-1">
            <label for="email" style="color: white;">Email</label><br>
            <input type="text" class="w-100 p-1" id="email">
          </div>
          <div class="form-group p-1">
            <label for="phone_number" style="color: white;">Phone Number</label><br>
            <input type="text" class="w-100 p-1" id="phone_number">
          </div>
      </div>
      <div class="col-md-6 float-left">
          <div class="form-group p-1">
            <label for="password" style="color: white;">Password</label><br>
            <input type="password" class="w-100 p-1" id="password">
          </div>
          <div class="form-group p-1">
            <label for="confirm_password" style="color: white;">Confirm Password</label><br>
            <input type="password" class="w-100 p-1" id="confirm_password">
          </div>
          <div class="form-group p-1">
            <input type="checkbox"> 
            <a href="#" class="link px-2">I accept the terms and condition</a>
          </div>
          <div class="form-group p-2">
            <button class="font-weight-bold button_blue align-items-center py-1 px-5 w-40" style="color: white;">SIGN UP</button>
          </div>
      </div>
    </div>
      
  </div>
</div>
<script>
  function handleScreenSizeChange() {
    const screenWidth = window.innerWidth;

    if (screenWidth <= 1021) {
      document.getElementById("sign_in_right_side").style.display = "none";
      document.getElementById("sign_in_left_side").classList.remove("col-md-4");
      document.getElementById("sign_in_left_side").classList.add("col-md-7");
    } else {
      // Show sign_in_right_side and reset sign_in_left_side
      document.getElementById("sign_in_right_side").style.display = "block";
      document.getElementById("sign_in_left_side").classList.remove("col-md-7");
      document.getElementById("sign_in_left_side").classList.add("col-md-4");
    }
  }

  handleScreenSizeChange();
  window.addEventListener("resize", handleScreenSizeChange);
</script>