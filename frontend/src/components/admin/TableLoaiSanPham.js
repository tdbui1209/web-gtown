import React, { useState, useEffect } from "react";

const TableLoaiSanPham = () => {
  const [data, setData] = useState([]);
  useEffect(() => {
    fetch('http://42.117.108.99:5000/products/categories')
      .then(response => response.json())
      .then(json => setData(json))
      .catch(error => console.error(error))
  }, []);

  return (
    <div className="col-md-12 overflow-auto">
      <table className="table table-striped table-bordered">
        <thead>
          <tr>
            <th><i className="bi bi-key-fill"></i> Mã</th>
            <th>Tên loại sản phẩm</th>
            <th className="text-center">Hành động</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr key={item.id}>
              <td className="text-center">{item.id}</td>
              <td className="align-items-center">{item.product_category_name}</td>
              <td className="text-center">
                <a href="#">Sửa</a> |
                <a href="#">Xóa</a>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default TableLoaiSanPham;
