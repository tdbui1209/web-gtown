<?php

$apiUrl = 'http://42.112.50.29:5000/categories/';

$response = file_get_contents($apiUrl);

if ($response === false) {
    echo 'Error fetching data.';
} else {
    // Xử lý dữ liệu response ở đây
    echo $response;
}

?>
