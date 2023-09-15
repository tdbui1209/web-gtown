import React from "react";
import Navbar from "../components/admin/Navbar";
import FormQuanLyLoaiSanPham from "../components/admin/FormQuanLyLoaiSanPham";
import TableLoaiSanPham from "../components/admin/TableLoaiSanPham";

const QuanLyLoaiSanPham = () =>{
  return(
    <div>
      <Navbar/>
      <FormQuanLyLoaiSanPham/>
      <TableLoaiSanPham/>
    </div>
  );
}

export default QuanLyLoaiSanPham;