import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import CardMedia from '@mui/material/CardMedia';
import { CardActionArea } from '@mui/material';

const CBKCTryoutDetail = ({ name, date, venue, location, img, description, actionBtns }) => {
	return (
		<>
			<Card sx={{ minWidth: 275, backgroundColor: '#f5f5f5' }}>
				<CardActionArea sx={{ display: 'flex', flexDirection: 'row-reverse', justifyContent: 'space-between' }}>
					<Box>
						<CardMedia component='img' height='250' image={`${import.meta.env.VITE_API_URL}${img}`} alt={name} />
					</Box>
					<CardContent
						sx={{
							display: 'flex',
							flexDirection: 'column',
							minHeight: '250px',
							justifyContent: 'space-between',
							maxWidth: '50%',
						}}>
						<Box
							sx={{ display: 'flex', height: '50%', flexDirection: 'column', justifyContent: 'space-between' }}>
							<Typography variant='h1' fontSize={'40px'} component='div' sx={{ mb: 1.5 }}>
								{name}
							</Typography>

							<Typography variant='h6' sx={{ color: 'text.secondary' }}>
								{date}
							</Typography>
							<Typography variant='h6' sx={{ color: 'text.secondary' }}>
								{location}
							</Typography>
							<Typography variant='h6' sx={{ color: 'text.secondary' }}>
								{venue}
							</Typography>
							<Typography variant='p' sx={{ color: 'text.secondary' }}>
								{description}
							</Typography>
						</Box>
						<Box>
							<CardActions>{actionBtns}</CardActions>
						</Box>
					</CardContent>
				</CardActionArea>
			</Card>
		</>
	);
};

export default CBKCTryoutDetail;
