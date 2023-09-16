import React from "react";
import { useRef } from "react";
import { Link } from "react-router-dom";
import '../css/admin/color.css';
import '../css/admin/style.css';
import Logo from "../../assets/img/logoGtown.png";
const Navbar = () => {
  const navRef = useRef();
  // const showNavBar = () => {
  //   if (window.innerWidth <= 1024) {
  //     navRef.current.classList.toggle("responsive_nav");
  //   }
  // }
  const showNavBar = () => {
    navRef.current.classList.toggle("responsive_nav");
  }
  const hideNavBar = () => {
    navRef.current.classList.remove("responsive_nav");
  }
  return(
    <header id="header">
        <img src={Logo} alt="adminLogo" className="logoShop"/>
        <nav id="nav" ref={navRef}>
            <a href="/trang_chu" className="navItem font-weight-bold">TRANG CHỦ</a>
            <a href="/quan_ly_loai_san_pham" className="navItem font-weight-bold">LOẠI SẢN PHẨM</a>
            <a href="/quan_ly_san_pham" className="navItem font-weight-bold">SẢN PHẨM</a>
            <a href="/quan_ly_nguoi_dung" className="navItem font-weight-bold">NGƯỜI DÙNG</a>
            <a href="/quan_ly_nha_san_xuat" className="navItem font-weight-bold">NGƯỜI DÙNG</a>
            <a href="/quan_ly_tin_tuc" className="navItem font-weight-bold">TIN TỨC</a>
            <button className="nav_btn nav_close_btn" onClick={showNavBar}>
              <i className="bi bi-x"></i>
            </button>
        </nav>
        <div>
          <button className="nav_btn" onClick={hideNavBar}>
            <i className="bi bi-list icon-admin"></i>
          </button>
          <button className="sign_out_btn">
            <i className="bi bi-box-arrow-right icon-admin"></i>
          </button>
        </div>
    </header>
  );
}
export default Navbar;