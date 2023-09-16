import React from "react";
import { useRef } from "react";
import '../css/admin/color.css';
import '../css/admin/style.css';
import Logo from "../../assets/img/logoGtown.png";
const Navbar = () => {
  const navRef = useRef();
  const showNavBar = () =>{
    navRef.current.classList.toggle("responsive_nav");
  }
  // const hideNavbar =()=>{
  //   navRef.current.classList.remove("responsive_nav")
  // }
  return(
    <header id="header">
        <img src={Logo} alt="adminLogo" className="logoShop"/>
        <nav id="nav" ref={navRef}>
            <a href="abc" className="navItem font-weight-bold">TRANG CHỦ</a>
            <a href="abc" className="navItem font-weight-bold">LOẠI SẢN PHẨM</a>
            <a href="abc" className="navItem font-weight-bold">NHÀ SẢN XUẤT</a>
            <a href="abc" className="navItem font-weight-bold">SẢN PHẨM</a>
            <a href="abc" className="navItem font-weight-bold">NGƯỜI DÙNG</a>
            <a href="abc" className="navItem font-weight-bold">TIN TỨC</a>
            <button className="nav_btn nav_close_btn" onClick={showNavBar}>
              <i className="bi bi-x"></i>
            </button>
        </nav>
        <button className="nav_btn" onClick={showNavBar}>
          <i className="bi bi-list icon-admin"></i>
        </button>
        {/* <button className="sign_out_btn">
          <i className="bi bi-box-arrow-right icon-admin"></i>
        </button> */}
    </header>
  );
}
export default Navbar;