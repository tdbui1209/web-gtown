import React, { useEffect } from "react";
import BackGroundSignIn from "../../assets/img/backgroundSignIn.jpg";
import "../css/admin/color.css";
import "../css/admin/style.css";

const FormDangKy = () => {
  useEffect(() => {
    document.body.classList.add('body_signin_signup');
  }, []);

  return (
    <div className="container">
      <div className="row d-flex justify-content-center align-items-center" style={{ minHeight: "100vh" }}>
        <div className="col-md-12 p-5" id="sign_up_container">
          <div className="col-md-12 p-3">
            <h2 style={{ color: "white" }} className="p-2">Sign Up</h2>
          </div>
          <div className="col-md-6 float-left">
            <div className="form-group">
              <label htmlFor="user_name" style={{ color: "white" }}>User name</label><br />
              <input type="text" className="w-100 p-1" id="user_name" />
            </div>
            <div className="form-group p-1">
              <label htmlFor="email" style={{ color: "white" }}>Email</label><br />
              <input type="text" className="w-100 p-1" id="email" />
            </div>
            <div className="form-group p-1">
              <label htmlFor="phone_number" style={{ color: "white" }}>Phone Number</label><br />
              <input type="text" className="w-100 p-1" id="phone_number" />
            </div>
          </div>
          <div className="col-md-6 float-left">
            <div className="form-group p-1">
              <label htmlFor="password" style={{ color: "white" }}>Password</label><br />
              <input type="password" className="w-100 p-1" id="password" />
            </div>
            <div className="form-group p-1">
              <label htmlFor="confirm_password" style={{ color: "white" }}>Confirm Password</label><br />
              <input type="password" className="w-100 p-1" id="confirm_password" />
            </div>
            <div className="form-group p-1">
              <input type="checkbox" />
              <a href="#" className="link px-2">I accept the terms and condition</a>
            </div>
            <div className="form-group p-2">
              <button className="font-weight-bold button_blue align-items-center py-1 px-5 w-40" style={{ color: "white" }}>SIGN UP</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default FormDangKy;
