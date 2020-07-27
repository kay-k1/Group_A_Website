<!-- virus database webpage -->
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <meta charset="UTF-8">
  <title>Virus Database</title>
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
<h2>SARS-CoV-2 Virus Database</h2>

<h3>The database table below shows sequence records from individuals all over the world who have been infected with COVID-19, each sequencne has a unique accession number.
    Our customily designed database allows you to search by location using the search bar displayed below. When typing the location in the 
    search bar, if you want to type a more specific location with the region for e.g. Germany: Dusseldorf please put a space between the : and the D otherwise no search results will show up. This applies
    to all specific locations
</h3>

<h3>Research has shown there is a variant of COVID-19 named D614G and this variant is now highly frequent in the majority 
    of infected individuals around the world. The D614G variant arises from a mutation in the SARS-CoV-2 viral genome, specifically in the viruses 
    spike protein. Various research and studies have shown that the D614G variant of COVID-19 is signifcantly more infectious than the other variation of the Covid-19 virus
    D614. In the database table below there is a column named D614G, the rows with a G represent that the individual has been infected with the D614G variant. If however the row has a D that means 
    the variant is a D614 variant, some rows have a letter other than a D or a G and unfortunately for some rows there is no letter in that column.This was because varaint calling for that sequence was not possible. For 
    more infromation on the D614G variant visit the D614G Variant page in the website. 
</h3>

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


#allows the user to search within the database by adding their input to the SQL command   
     if(isset($_GET['search'])){
        $searchKey = $_GET['search'];
        $sql = "SELECT accession,location,strain_id,collection_date,D614G FROM virus WHERE location LIKE '%{$searchKey}%'";
     }else
     $sql = "SELECT * FROM virus";
     $result = mysqli_query($connection,$sql);
   ?>

<!-- creates search space for user input for above php code -->
   <form action="" method="GET"> 
     <div class="col-md-6">
        <input type="text" name="search" class='form-control' placeholder="Search By Location (for e.g. China)" value=<?php echo @$_GET['search']; ?> > 
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
     <th>Accession Number</th>
     <th>Location</th>
     <th>Strain ID</th>
     <th>Collection Date</th> 
     <th>D614G Variant</th>  
  </tr>
  <?php while( $row = $result->fetch_object() ): ?>
  <tr>
     <td><?php echo $row->accession ?></td>
     <td><?php echo $row->location ?></td>
     <td><?php echo $row->strain_id ?></td>
     <td><?php echo $row->collection_date ?></td>
     <td><?php echo $row->D614G ?></td>
  </tr>
  <?php endwhile; ?>
</table>
</div>
</div>
</div>
</body>
</html>
