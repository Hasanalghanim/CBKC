import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import axios from 'axios';
import { useQuery } from '@tanstack/react-query';
import CircleLoader from '../../../util/CircleLoader';
import { Link } from 'react-router';

const TryoutsTableMobile = () => {
	const csrfToken = window.csrfToken;
	const { data, isError, isLoading } = useQuery({
		queryKey: ['Tryouts'],
		queryFn: async () => {
			const { data } = await axios.get(`${import.meta.env.VITE_API_URL}/tryouts/api/TryoutEventList`, {
				headers: {
					'X-CSRFToken': csrfToken,
				},
			});
			return data;
		},
	});

	if (isLoading) return <CircleLoader />;
	if (isError) return <CircleLoader error />;

	return (
		<>
			{data.map((event) => {
				return (
					<>
						<Card
							key={event.id}
							sx={{
								height: '100%',
								display: 'flex',
								flexDirection: 'column',
								justifyContent: 'space-between',
							}}>
							<CardMedia
								component='img'
								height='250'
								image={`${import.meta.env.VITE_API_URL}${event.banner}`}
								alt={event.name}
							/>

							<CardContent sx={{ flexGrow: 1 }}>
								<Typography gutterBottom variant='h5' component='div' noWrap>
									{event.name}
								</Typography>

								<Typography variant='body2' sx={{ color: 'text.secondary' }} noWrap>
									{event.venue}
								</Typography>

								<Typography variant='body2' sx={{ color: 'text.secondary' }} noWrap>
									{event.location}
								</Typography>

								<Typography
									variant='body2'
									sx={{
										color: 'text.secondary',
										overflow: 'hidden',
										textOverflow: 'ellipsis',
										display: '-webkit-box',
										WebkitLineClamp: 3, // limit to 3 lines
										WebkitBoxOrient: 'vertical',
									}}>
									{event.description}
								</Typography>
							</CardContent>

							<CardActions>
								<Link to={`/dashboard/tryouts_tab/${event.slug}`} style={{ textDecoration: 'none' }}>
									<Button size='small' variant='contained'>
										Events Detail
									</Button>
								</Link>
							</CardActions>
						</Card>
					</>
				);
			})}
		</>
	);
};

export default TryoutsTableMobile;
