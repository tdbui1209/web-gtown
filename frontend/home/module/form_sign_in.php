<div class="container">
  <div class="row d-flex justify-content-center align-items-center" style="min-height: 100vh;">
      <div class="col-md-4 p-5" id="sign_in_left_side">
        <h2 style="color: white;" class="p-2">Sign In</h2>
        <div class="form-group p-2">
          <label for="user_name" style="color: white;">User name</label><br>
          <input type="text" class="w-100 p-2" id="user_name">
        </div>
        <div class="form-group p-2">
          <label for="password" style="color: white;">Password</label><br>
          <input type="password" class="w-100 p-2" id="password">
        </div>
        <div class="form-group p-2">
          <a href="#" style="font-size: 9pt;" class="link">FORGOT PASSWORD?</a>
        </div>
        <div class="form-group p-2">
          <button class="font-weight-bold button_blue align-items-center py-1 px-5 w-100" style="color: white;">SIGN IN</button>
        </div>
        <div class="form-group" style="color: white; font-size: 9pt;">
          Don't have any account? <a href="#" class="link">Sign up</a>
        </div>
      </div>
      <div class="col-md-7 p-0" id="sign_in_right_side">
        <img class="sign_in_background" src="../../img/home/backgroundSignIn.jpg">
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