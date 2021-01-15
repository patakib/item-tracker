function filterSupplier() {
  // Declare variables
  let supplierSearch = document.getElementById("supplierSearch");
  let filter = supplierSearch.value.toUpperCase();
  let table = document.getElementById("myTable");
  let tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    let td = tr[i].getElementsByTagName("td")[8];
    if (td) {
      let txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
