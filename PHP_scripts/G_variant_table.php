<!-- variant database webpage -->
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <meta charset="UTF-8">
  <title>G Variant Table</title>
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

h3 {
font-size:20px;
text-align:justify;
line-height:25px;
margin-left:12px;
margin-right:12px;
}
</style>
<body>
<h2>SARS-CoV-2 G Variant Table</h2>

<h3>The table below shows sequence records from individuals all over the world who have been infected with COVID-19, specifically by the variant of coronavirus where 
    the spike glycoprotein of the SARS-CoV-2 viral genome has a G (Glycine) at residue 614, this is the more infectious variant of coronavirus. <br><br>When typing the location in the 
    search bar, if you want to type a more specific location with the region for e.g. Germany: Dusseldorf please put a space between the : and the D otherwise no search results will show up.This applies
    to all specific locations. 
</h3>


<div class="container">
   <div class="row">
   <div class="col-md-8 col-md-offset-2" style="margin-top: 5%;">
   <div class="row">

  
<?php
#connects to databse on lamp server
$dbServername = "localhost";
$dbUsername = "lampuser";
$dbPassword = "changeme";
$dbName = "SRP";

$connection = mysqli_connect($dbServername,$dbUsername,$dbPassword,$dbName);


#allows the user to search within the database by adding their input to the SQL command      
     if(isset($_GET['search'])){
        $searchKey = $_GET['search'];
        $sql = "SELECT accession,location,strain_id,collection_date FROM virus WHERE location LIKE '%{$searchKey}%' AND D614G='G' ORDER BY collection_date ASC";
     }else
     $sql = "SELECT * FROM virus";
     $result = mysqli_query($connection,$sql);
   ?>

<!-- creates search space for user input for above php code -->
   <form action="" method="GET"> 
     <div class="col-md-6">
        <input type="text" name="search" class='form-control' placeholder="Search By Location (for e.g. Germany)" value=<?php echo @$_GET['search']; ?> > 
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
     <th>Acession Number</th>
     <th>Location</th>
     <th>Strain ID</th>
     <th>Collection Date</th> 
  </tr>
  <?php while( $row = $result->fetch_object() ): ?>
  <tr>
     <td><?php echo $row->accession ?></td>
     <td><?php echo $row->location ?></td>
     <td><?php echo $row->strain_id ?></td>
     <td><?php echo $row->collection_date ?></td>
  </tr>
  <?php endwhile; ?>
</table>
</div>
</div>
</div>
</body>
</html>
