var tables, i;
tables = document.getElementsByTagName('table');
for (i=0;i<tables.length;i++) {
  tables[i].className = 'table table-bordered table-hover table-striped table-responsive';
}