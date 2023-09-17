import React from "react";
//Thay đổi title tương ứng với mỗi Route
import { Helmet } from 'react-helmet';
import Navbar from "../components/admin/Navbar";
import FormQuanLyLoaiSanPham from "../components/admin/FormQuanLyLoaiSanPham";
import TableLoaiSanPham from "../components/admin/TableLoaiSanPham";

const QuanLyLoaiSanPham = () =>{
  return(
    <div>
      <Helmet>
        <title>Quản lý loại sản phẩm</title>
      </Helmet>
      <Navbar/>
      <FormQuanLyLoaiSanPham/>
      <TableLoaiSanPham/>
    </div>
  );
}

export default QuanLyLoaiSanPham;