import { useQuery } from '@tanstack/react-query';
import { useParams } from 'react-router';
import CircleLoader from '../../../util/CircleLoader';
import axios from 'axios';
import { Box, Card, CardContent, Grid, Typography } from '@mui/material';
import TryoutFIghtersCard from './TryoutFIghtersCard';

const TryoutFightTableMobile = ({ eventId }) => {
	const csrfToken = window.csrfToken;
	const { slug } = useParams();

	const { data, isError, isLoading, error } = useQuery({
		queryKey: ['TryoutsFighters', slug],
		queryFn: async () => {
			try {
				const { data } = await axios.get(
					`${import.meta.env.VITE_API_URL}/tryouts/api/TryoutRegistrantList/${eventId}/`,
					{
						headers: {
							'X-CSRFToken': csrfToken,
						},
					}
				);
				return data;
			} catch (error) {
				console.error('Error fetching tryout details:', error);
				throw error;
			}
		},
		enabled: !!slug,
	});

	if (isLoading) return <CircleLoader />;
	if (isError) return <CircleLoader error />;

	return (
		<Card sx={{ minWidth: 275, backgroundColor: '#f5f5f5' }}>
			<CardContent
				sx={{
					display: 'flex',
					flexDirection: 'column',
					minHeight: '250px',
					gap: 2.5,
				}}>
				<Typography variant='h4' sx={{ color: 'text.secondary' }}>
					Fighters
				</Typography>
				<Box>
					<Grid container spacing={1}>
						{data.map((fighter) => {
							return (
								<Grid item size={6} key={fighter.id}>
									<TryoutFIghtersCard fighter={fighter} />
								</Grid>
							);
						})}
					</Grid>
				</Box>
			</CardContent>
		</Card>
	);
};

export default TryoutFightTableMobile;
