import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import CBKCDialog from '../../../components/CBKCDialog';
import { formatDateTimeWithTimezone } from '../../../util/formatDates';

const TryoutFIghtersCard = ({ fighter }) => {
	return (
		<>
			<Card sx={{ maxWidth: 345, overflow: 'hidden' }}>
				<CardMedia
					sx={{ height: 200 }}
					image={`${import.meta.env.VITE_API_URL}${fighter.image}`}
					title={fighter.first_name}
				/>
				<CardContent>
					<Typography gutterBottom variant='h5' component='div'>
						{fighter.first_name} {fighter.last_name}
					</Typography>
					<Typography variant='body2' sx={{ color: 'text.secondary', wordWrap: 'break-word' }}>
						Weight: {fighter.weight_class}
					</Typography>
					<Typography variant='body2' sx={{ color: 'text.secondary', wordWrap: 'break-word' }}>
						{fighter.phone}
					</Typography>
					<Typography variant='body2' sx={{ color: 'text.secondary', wordWrap: 'break-word' }}>
						{fighter.email}
					</Typography>
				</CardContent>
				<CardActions>
					<CBKCDialog
						buttonName={'View Fighter'}
						popUpTitle={`${fighter.first_name} ${fighter.last_name}`}
						noSubmitBtn
						popupText={''}
						dialogSize={'md'}>
						{({}) => (
							<>
								<Typography variant='body2' sx={{ color: 'text.secondary', wordWrap: 'break-word' }}>
									Weight: {fighter.weight_class}
								</Typography>
								<Typography variant='body2' sx={{ color: 'text.secondary', wordWrap: 'break-word' }}>
									Phone Number: {fighter.phone}
								</Typography>
								<Typography variant='body2' sx={{ color: 'text.secondary', wordWrap: 'break-word' }}>
									Email: {fighter.email}
								</Typography>
								<Typography variant='body2' sx={{ color: 'text.secondary', wordWrap: 'break-word' }}>
									Experience (yrs): {fighter.experience_years}
								</Typography>
								<Typography variant='body2' sx={{ color: 'text.secondary', wordWrap: 'break-word' }}>
									Date Registered: {formatDateTimeWithTimezone(fighter.date_registered)}
								</Typography>
							</>
						)}
					</CBKCDialog>
				</CardActions>
			</Card>
		</>
	);
};

export default TryoutFIghtersCard;
