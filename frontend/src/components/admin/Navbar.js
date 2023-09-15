import React from "react";
import '../css/admin/color.css';
import '../css/admin/style.css';
import Logo from "../../assets/img/logoGtown.png";
const Navbar = () => {
  return(
    <header>
      <div className="container-fluid d-flex align-items-center d-flex py-3" id="header">
        <div className="col-md-2" id="header-left" >
          <img src={Logo} alt="adminLogo" className="logoShop"/>
        </div>
        <div className="col-md-8 d-flex justify-content-around" id="header-center">
          <a href="abc" className="navItem font-weight-bold">TRANG CHỦ</a>
          <a href="abc" className="navItem font-weight-bold">LOẠI SẢN PHẨM</a>
          <a href="abc" className="navItem font-weight-bold">NHÀ SẢN XUẤT</a>
          <a href="abc" className="navItem font-weight-bold">SẢN PHẨM</a>
          <a href="abc" className="navItem font-weight-bold">NGƯỜI DÙNG</a>
          <a href="abc" className="navItem font-weight-bold">TIN TỨC</a>
        </div> 
        <div className="col-md-2 px-5 text-right" id="header-right">
          <i class="bi bi-x-lg icon-admin"></i>
          <i class="bi bi-list icon-admin mr-5"></i>
          <i className="bi bi-box-arrow-right icon-admin"></i>
        </div>
      </div>
    </header>
  );
}
export default Navbar;