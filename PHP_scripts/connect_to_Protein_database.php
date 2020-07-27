<!-- protein database webpage -->
<!DOCTYPE html>
<html>

<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<meta charset="UTF-8">
<title> Protein Database</title>
</head>
<style>
table th {
font-size:15px;
text-align:center;
}
h2 {
font-size:80px;
text-align:center;
font-weight:bold;
text-decoration:underline;
}
</style>
<body>

<h2>SARS-CoV-2 Protein Database</h2>

<div class="container">
   <div class="row">
   <div class="col-md-8 col-md-offset-2" style="margin-top: 5%;">
   <div class="row">


<?php
#php code that connects to the database on the lamp server
$dbServername = "localhost";
$dbUsername = "lampuser";
$dbPassword = "changeme";
$dbName = "SRP";




$connection = mysqli_connect($dbServername,$dbUsername,$dbPassword,$dbName);

#allows the user to search within the database
if(isset($_GET['search'])){
        $searchKey = $_GET['search'];
        $sql = "SELECT protein_id,product,PDB_tag FROM protein WHERE PDB_tag LIKE '%$searchKey%' and PDB_tag !='null';";
     }else
     $sql = "SELECT protein_id,product,PDB_tag FROM protein WHERE PDB_tag !='null'";
     $result = mysqli_query($connection,$sql);

?>
<!-- creates search space for user input for above php code -->
 <form action="" method="GET"> 
     <div class="col-md-6">
        <input type="text" name="search" class='form-control' placeholder="Search By PDB_tag (for e.g. 6W37)" value=<?php echo @$_GET['search']; ?> > 
     </div>
     <div class="col-md-6 text-left">
      <button class="btn">Search</button>
     </div>
   </form>

   <br> 
   <br>
</div>

<!-- style of the table and which rows are to be shown -->
<table class="table table-bordered">
  <tr>
     <th>Protein ID</th>
     <th>Product</th>
     <th>PDB_tag</th>
  </tr>
  <?php while( $row = $result->fetch_object() ): ?>
  <tr>
     <td><?php echo $row->protein_id ?></td>
     <td><?php echo $row->product ?></td>
     <td><?php echo $row->PDB_tag ?></td>
  </tr>
  <?php endwhile; ?>
</table>
</div>
</div>
</div>

</body>

</html>
