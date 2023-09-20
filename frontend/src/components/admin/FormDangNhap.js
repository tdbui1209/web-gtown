import React from "react";
import { useEffect, useState } from "react";
import BackGroundSignIn from "../../assets/img/backgroundSignIn.jpg";
import '../css/admin/color.css';
import '../css/admin/style.css';
import { useNavigate } from "react-router-dom";
const FormDangNhap = () => {
  useEffect(()=>{
    document.body.classList.add('body_signin_signup');
  });
  const navigate = useNavigate();
  const navigateSignUp = () =>{
    navigate('/dang_ky');
  };
  return (
    <div className="container">
      <div className="row d-flex justify-content-center align-items-center" style={{ minHeight: "100vh" }}>
        <div className="col-md-4 p-5" id="sign_in_left_side">
          <h2 style={{ color: "white" }} className="p-2">ĐĂNG NHẬP</h2>
          <div className="form-group p-2">
            <label htmlFor="user_name" style={{ color: "white" }}>Tên tài khoản</label><br />
            <input type="text" className="w-100 p-2" id="user_name" />
          </div>
          <div className="form-group p-2">
            <label htmlFor="password" style={{ color: "white" }}>Mật khẩu</label><br />
            <input type="password" className="w-100 p-2" id="password" />
          </div>
          <div className="form-group p-2">
            <a href="#" className="link">QUÊN MẬT KHẨU?</a>
          </div>
          <div className="form-group p-2">
            <button className="font-weight-bold button_blue align-items-center py-1 px-5 w-100" style={{ color: "white" }}>ĐĂNG NHẬP</button>
          </div>
          <div className="form-group" style={{ color: "white", fontSize: "9pt" }}>
            Bạn chưa có tài khoản? <button onClick={navigateSignUp} className="link">Đăng ký</button>
          </div>
        </div>
        <div className="col-md-7 p-0" id="sign_in_right_side">
          <img className="sign_in_background" src={BackGroundSignIn} alt="Sign In Background" />
        </div>
      </div>
    </div>
  );
}

export default FormDangNhap;
