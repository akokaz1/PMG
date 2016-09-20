use Kubrick
go

select * from Tweets
where datepart(hh, [UTC Date]) between 11 and 20
 and datepart(dd, [UTC Date]) = 19
order by [UTC Date] asc
